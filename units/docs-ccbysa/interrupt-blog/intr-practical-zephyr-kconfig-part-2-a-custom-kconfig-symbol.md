---
id: "intr-practical-zephyr-kconfig-part-2-a-custom-kconfig-symbol"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): A custom Kconfig symbol"
summary: "In the previous sections, we examined Kconfig in detail. To wrap up this article, we'll create and use a custom, application-specific symbol in our application and build process."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#a-custom-kconfig-symbol"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the previous sections, we examined _Kconfig_ in detail. To wrap up this article, we'll create and use a custom, application-specific symbol in our application _and_ build process.

> **Note:** This section borrows from the [nRF Connect SDK Fundamentals lesson on configuration files](https://academy.nordicsemi.com/courses/nrf-connect-sdk-fundamentals/lessons/lesson-3-elements-of-an-nrf-connect-sdk-application/topic/configuration/) that is freely available in the [Nordic Developer Academy](https://academy.nordicsemi.com/). If you're looking for additional challenges, check out the available courses!

### Adding a custom configuration

[CMake automatically detects a `Kconfig` file](https://docs.zephyrproject.org/latest/develop/application/index.html#application-cmakelists-txt) if it is placed in the same directory of the application's `CMakeLists.txt`, and that is what we'll use for our own configuration file. If you want to place the `Kconfig` file somewhere else, you can customize this behavior using an absolute path for the `KCONFIG_ROOT` build system variable.

Similar to the file `zephyr/subsys/debug/Kconfig` of Zephyr's _debug_ subsystem, the `Kconfig` file specifies all available configuration options and their dependencies. We'll only specify a simple boolean symbol in the `Kconfig` file in our application's root directory. Please refer to the [official documentation](https://docs.zephyrproject.org/latest/build/kconfig/setting.html#setting-kconfig-configuration-values) for details about the `Kconfig` syntax:

```bash
$ tree --charset=utf-8 --dirsfirst -L 1
.
├── boards
├── src
├── CMakeLists.txt
├── Kconfig
├── extra0.conf
├── extra1.conf
├── prj.conf
└── prj_release.conf

$ cat Kconfig
```

```conf
mainmenu "Customized Menu Name"
source "Kconfig.zephyr"

menu "Application Options"
config USR_FUN
	bool "Enable usr_fun"
	default n
	help
	  Enables the usr_fun function.
endmenu
```

The skeleton of this `Kconfig` file is well explained in [step 4 in the "Application CMakeLists.txt" section in the official documentation](https://docs.zephyrproject.org/latest/develop/application/index.html#application-cmakelists-txt):

The statement _"mainmenu"_ defines a custom text that is used as our `Kconfig` main menu. It is shown, e.g., as a title in the build target `menuconfig`. We'll see this in a moment when we'll build our target and launch `menuconfig`.

The _"source"_ statement essentially includes the top-level Zephyr Kconfig file `zephyr/Kconfig.zephyr` and all of its symbols (all _"source"_ statements are relative to Zephyr's root directory). This is necessary since we're effectively replacing the `zephyr/Kconfig` file of the Zephyr base that is usually _parsed_ as the first file by _Kconfig_. We'll see this below when we look at the build output. The contents of the default root `Kconfig` file are quite similar to what we're doing right now:

```bash
$ cat $ZEPHYR_BASE/Kconfig
# -- hidden comments --
mainmenu "Zephyr Kernel Configuration"
source "Kconfig.zephyr"
```

By sourcing the `Kconfig.zephr` file, we're loading all _Kconfig_ menus and symbols provided with Zephr. Next, we declare our own menu between the _"menu"_ and _"endmenu"_ statements to group our application symbols. Within this menu, we declare our `USR_FUN` symbol, which we'll use to enable a function `usr_fun`.

Let's rebuild our application without configuring `USR_FUN` and have a look at the build output. A `--pristine` build is required to pick up the new `Kconfig` file:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build --pristine
```

```
Parsing /path/to/01_kconfig/Kconfig
Loaded configuration '/opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig'
Merged configuration '/path/to/01_kconfig/prj.conf'
Merged configuration '/path/to/01_kconfig/boards/nrf52840dk_nrf52840.conf'
Configuration saved to '/path/to/build/zephyr/.config'
Kconfig
```

Have a good look at the very first line of the _Kconfig_-related output:
* In our previous builds, this line indicated the use of Zephyr's default `Kconfig` file as follows:
  `Parsing /opt/nordic/ncs/v3.2.1/zephyr/Kconfig`,
* Whereas now it uses our newly created `Kconfig` file:
  `Parsing /path/to/01_kconfig/Kconfig`.

The remainder of the output should look familiar. When we look at the generated `zephyr/.config` file in our build directory, we see that the `USR_FUN` symbol is indeed set according to its default value `n`:

```bash
$ cat ../build/zephyr/.config
# Application Options
#
# CONFIG_USR_FUN is not set
# end of Application Options
```

The new, custom main menu name _"Customized Menu Name"_ is only visible in the interactive _Kconfig_ tools, such as `menuconfig`, and is not used within the generated `zephyr/.config` file. The interactive tools now also show our newly created menu and symbol.

As you can see in the below screenshot, the main menu has the name _"Customized Menu Name"_ and a new menu _"Application Options"_ is now available as the last entry of options:

```bash
$ west build -d ../build -t menuconfig
```




> **Notice:** It is also possible to source `Kconfig.zephyr` _after_ defining the application symbols and menus. This would have the effect that your options will be listed _before_ the Zephyr symbols and menus. In this section, we've sourced `Kconfig.zephr` before our own options.

### Configuring the application build using _Kconfig_

Now that we have our own `Kconfig` symbol, we can use it in the application's build process. Create two new files `usr_fun.c` and `usr_fun.h` in the `src` directory:

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── boards
│   ├── nrf52840dk_nrf52840.conf
│   └── nrf52840dk_nrf52840_release.conf
├── src
│   ├── main.c
│   ├── usr_fun.c
│   └── usr_fun.h
├── CMakeLists.txt
├── Kconfig
├── extra0.conf
├── extra1.conf
├── prj.conf
└── prj_release.conf
```

We're defining a simple function `usr_fun` that prints an additional message on boot using the newly created files:

```c
// Content of usr_fun.h
#pragma once

void usr_fun(void);
```

```c
// Content of usr_fun.c
#include "usr_fun.h"
#include <zephyr/kernel.h>

void usr_fun(void)
{
    printk("Message in a user function.\n");
}
```

Now, all that's left is to tell _CMake_ about our new files. Instead of always including these files when building our application, we can use our _Kconfig_ symbol `USR_FUN` to only include the files in the build if the symbol is enabled. Add the adding the following to `CMakeLists.txt`:

```cmake
target_sources_ifdef(
    CONFIG_USR_FUN
    app
    PRIVATE
    src/usr_fun.c
)
```

`target_sources_ifdef` is another _CMake_ extension from `zephyr/cmake/modules/extensions.cmake`: It conditionally includes our files in the build in case `CONFIG_USR_FUN` is defined. Since the symbol `USR_FUN` is _disabled_ by default, our build currently does not include `usr_fun`.

### Using the application's `Kconfig` symbol

Let's first extend our `main.c` file to use `usr_fun` regardless of any configuration options:

```c
#include <zephyr/kernel.h>
#include "usr_fun.h"

#define SLEEP_TIME_MS 100U

int main(void)
{
    printk("Message in a bottle.\n");
    usr_fun();

    while (1)
    {
        k_msleep(SLEEP_TIME_MS);
    }
}
```

Unsurprisingly, building this application fails since `usr_fun.c` is not included in the build:

```bash
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build --pristine
```

```
[158/168] Linking C executable zephyr/zephyr_pre0.elf
FAILED: zephyr/zephyr_pre0.elf zephyr/zephyr_pre0.map
--snip--
/path/to/ld.bfd: app/libapp.a(main.c.obj): in function `main':
/path/to/main.c:9: undefined reference to `usr_fun'
collect2: error: ld returned 1 exit status
ninja: build stopped: subcommand failed.
FATAL ERROR: command exited with status 1: /path/to/cmake --build /path/to/build
```

We have two possibilities to fix our build: The first possibility is to enable `USR_FUN` in our kernel configuration, e.g., in our `prj.conf` file:

```conf
# --snip--
CONFIG_USR_FUN=y
```

This, however, defeats the purpose of having a configurable build: The build would still fail in case we're not enabling `USR_FUN`. Instead, we can also use the `USR_FUN` symbol within our code to only conditionally include parts of our application:

```c
#include <zephyr/kernel.h>

#ifdef CONFIG_USR_FUN
#include "usr_fun.h"
#endif

#define SLEEP_TIME_MS 100U

int main(void)
{
    printk("Message in a bottle.\n");

#ifdef CONFIG_USR_FUN
    usr_fun();
#endif

    while (1)
    {
        k_msleep(SLEEP_TIME_MS);
    }
}
```

Now, our build succeeds for either configuration of the `USR_FUN` symbol. Clearly, we could also use the same approach as `printk` and provide an empty function or definition for `usr_fun` instead of adding conditional statements to our application.

> **Note:** The application builds and links, but you won't see any output on the serial console in case you've followed along; The _Kconfig_ symbols responsible for the serial output are still disabled within `prj.conf` and the board-specific fragment. Feel free to update your configuration, e.g., by enabling the debug output for normal builds while disabling it for the "release" build!

To understand why we can use the `CONFIG_USR_FUN` definition, we can have a look at the compiler commands used to compile `main.c`. Conveniently (as mentioned in the previous article), by default, Zephyr enables the _CMake_ variable [`CMAKE_EXPORT_COMPILE_COMMANDS`](https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html). The compiler command for `main.c` is thus captured by the `compile_commands.json` in our build directory:

```json
{
  "directory": "/path/to/build",
  "command": "/path/to/bin/arm-zephyr-eabi-gcc --SNIP-- -o CMakeFiles/app.dir/src/main.c.obj -c /path/to/main.c",
  "file": "/path/to/main.c"
},
```

Within the large list of parameters passed to the compiler, there is also the `-imacros` option specifying the `autoconf.h` Kconfig header file:

```
-imacros /path/to/build/zephyr/include/generated/autoconf.h
```

This header file contains the configured value of the `USR_FUN` symbol as a macro:

```c
// --snip---
#define CONFIG_USR_FUN 1
```

Looking at the [official documentation of the `-imacros` option for `gcc`](https://gcc.gnu.org/onlinedocs/gcc/Preprocessor-Options.html), you'll find that this option acquires all the macros of the specified header without also processing its declarations. Thus, all macros within the `autoconf.h` files are also available at compile time.
