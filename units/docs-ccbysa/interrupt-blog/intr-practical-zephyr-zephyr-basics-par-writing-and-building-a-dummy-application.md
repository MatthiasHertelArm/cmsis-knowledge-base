---
id: "intr-practical-zephyr-zephyr-basics-par-writing-and-building-a-dummy-application"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Zephyr Basics (Part 1): Writing and building a dummy application"
summary: "Our main.c file contains our application code. We'll just provide a dummy application that does nothing but send our MCU back to sleep repeatedly:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-10-practical_zephyr_basics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_basics#writing-and-building-a-dummy-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Source code

Our `main.c` file contains our application code. We'll just provide a dummy application that does nothing but send our MCU back to sleep repeatedly:

```c
#include <zephyr/kernel.h>

int main(void)
{
    while (1)
    {
        k_msleep(100U); // Sleep for 100 ms.
    }
}
```

Notice that this is a plain infinite loop and it doesn't make any use of threads yet - something that you'll change in a more complex application: In the end, it makes limited sense to use Zephyr without its operating system. For now, keep in mind that [applications _can_ operate without threads](https://docs.zephyrproject.org/latest/kernel/services/threads/nothread.html#nothread), though this severely limits the functionality provided by Zephyr.

### Build configuration

Now we come to the heart of this first step towards Zephyr: The build configuration. In case you're not familiar at all with *CMake*, there are several articles and even books about ["Effective Modern CMake"](https://gist.github.com/mbinna/c61dbb39bca0e4fb7d1f73b0d66a4fd1): *CMake* has evolved significantly, and only certain patterns should be used for new applications. We won't explain *CMake* here, but if you're an experienced developer, you should understand the basics just fine when reading along.

Let's go through the steps to create our `CMakeLists.txt` for this empty application:

```cmake
cmake_minimum_required(VERSION 3.20.0)

set(BOARD nrf52840dk/nrf52840)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
```

- `cmake_minimum_required` just indicates the allowed CMake versions. Zephyr has its requirements and maintains its minimal required CMake version in `zephyr/cmake/modules/zephyr_default.cmake`.
- The `set` function writes the board we're building our application for to the variable `BOARD`. This step is optional and can be specified during the build step as a parameter. `nrf52840dk/nrf52840` is Zephyr's name for the [nRF52840 development kit](https://www.nordicsemi.com/Products/Development-hardware/nrf52840-dk).
- Then, we load Zephyr using the `find_package` function. In our [setup script](#creating-a-setup-script), we've exported the `ZEPHYR_BASE` environment variable, which is now passed as a hint to the `find_package` function to locate the correct Zephyr installation.

> **Note:** There are several ways to use the Zephyr CMake package, each of which is described in detail in [Zephyr's CMake package documentation](https://docs.zephyrproject.org/latest/build/zephyr_cmake_package.html). You can also have a look at the [Zephyr CMake package source code](https://docs.zephyrproject.org/latest/build/zephyr_cmake_package.html#zephyr-cmake-package-source-code) for details.

As mentioned, setting the `BOARD` variable is optional and usually not done. The value for the `BOARD` can be chosen in different ways, e.g., using an environment variable, or passed as a parameter during the build. The Zephyr build system determines the final value for `BOARD` in a pre-defined order; refer to the [documentation for the application CMakeLists.txt](https://docs.zephyrproject.org/latest/develop/application/index.html#application-cmakelists-txt) for details.

> **Note**: Zephyr's goal is to support multiple boards and multiple MCUs. Once we switch to using _West_ for building, it makes sense to pass the board as a parameter and _not_ specify it in `CMakeLists.txt`. In case you're having trouble remembering the exact board name, you can always dump the list of supported boards using the command `west boards`.

Now that Zephyr is available, we can go ahead and add the application:

```cmake
project(
    EmptyApp
    VERSION 0.1
    DESCRIPTION "Empty zephyr application."
    LANGUAGES C
)

target_sources(
    app
    PRIVATE
    src/main.c
)
```

- The `project` function defines the name and settings of the application project.
- Then, we simply need to add our sources to the `app` target.

But wait. What's this `app` target, and why don't we need to specify an executable? This is all done within the Zephyr CMake package: The package already defines your executable and also provides this `app` library target which is intended to be used for all application code. At the time of writing, this `app` target is constructed by the following CMake files in the Zephyr project:

`zephyr/cmake/modules/kernel.cmake`
```cmake
zephyr_library_named(app)
```

`zephyr/cmake/modules/extensions.cmake`
```cmake
macro(zephyr_library_named name)
  set(ZEPHYR_CURRENT_LIBRARY ${name})
  add_library(${name} STATIC "")
  zephyr_append_cmake_library(${name})
  target_link_libraries(${name} PUBLIC zephyr_interface)
endmacro()
```

### Building the application

With the `CMakeLists.txt` in place, we can build the application. There are several ways to do this and if you're familiar with CMake, the below commands are no surprise. What we want to show, however, is the slight differences between using CMake or _West_ when building your application. Let's first use CMake:

#### Building with CMake

```bash
$ cmake -B ../build
$ cmake --build ../build -- -j4
```

> **Note:** The [GitHub repository](https://github.com/lmapii/practical-zephyr) uses subfolders for all example applications. Using a build directory `../build` located in the root of the repository allows an editor such as `VS Code` to pick up the compile commands independent of the example that is being built. In case you're using `VS Code`, have a look at the provided [`settings.json`](https://github.com/lmapii/practical-zephyr/blob/main/.vscode/settings.json) file.

With this, the `../build` folder contains the application built for the `BOARD` specified in the `CMakeLists.txt` file. The following command allows passing the `BOARD` to CMake directly and thereby either **overrides** a given `set(BOARD ...)` instruction or provides the `BOARD` in case it hasn't been specified at all:

```bash
# Build for a specific board determined during build time.
$ cmake -B ../build -DBOARD=nrf52dk_nrf52832
```

Let's try to build the application using _West_:

```bash
$ rm -rf ../build
$ west build -d ../build
WARNING: This looks like a fresh build and BOARD is unknown; so it probably won't work. To fix, use --board=<your-board>.
Note: to silence the above message, run 'west config build.board_warn false'
<truncated output>
```

> **Note:** The default build directory of _West_ is a `build` folder within the same directory. If run without `-d ../build`, _West_ will create a `build` folder in the current directory for the build.

The build seems to succeed, but there's a warning indicating that no board has been specified. How is that possible? _West_ typically still expects a "board configuration" or the `--board` parameter. The reason for this is simple: _West_ is much more than just a wrapper for CMake and therefore doesn't parse the provided `CMakeLists.txt` file - where we specified the `BOARD`. It just warns you that you may have forgotten to specify the `board` but still proceeds to call CMake.

Before looking another step deeper into West, comment or **delete** the `set(BOARD ...)` instruction in your `CMakeLists.txt` file.


#### Building with West

As mentioned, _West_ needs an indication of which board is being used by your project. Just like plain CMake, this could be done by specifying the `BOARD` as an environment variable or by passing the board to `west build`:

```bash
# pass the board as argument
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build
# or using an environment variable
$ export BOARD=nrf52840dk/nrf52840
$ west build -d ../build
```

Underneath, _West_ sets up the build directory and then simply invokes CMake. Thus, everything build-related is still plain old CMake. The above builds run without warning.

> **Note:** The `build` command is actually a so-called [_West_ extension command](https://docs.zephyrproject.org/latest/develop/west/zephyr-cmds.html) and is not built into _West_ by default. You could thus, e.g., use _West_ without Zephyr as a repository manager in a different context. Zephyr provides extension commands such as [`build`, `flash`, and `debug`](https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html) in its own _West_ extension such that applications can be built, flashed, and debugged in the same way, independent of, e.g., the debugger or programmer that is used. If you're interested in how Zephyr's extensions work, have a look at `zephyr/scripts/west-commands.yml` and the corresponding _West_ extension scripts.

> **Note:** Zephyr uses so called [system builds](https://docs.zephyrproject.org/latest/build/sysbuild/index.html) by default. In simple words, system builds combine one or more builds into a hierarchical build, e.g., if you're using a bootloader like `mcuboot` then you can build the application and the bootloader together using system build. For the remainder of this article series you'll find that we _disable_ system builds using `--no-sysbuild`. We need to do this since we'll be looking through files in our build folder and using system builds changes these paths significantly.

Once the build folder has been created using any of the above commands, it is no longer necessary to pass the board to _West_:

```bash
# in case the build directory exists already ...
$ if test -d ../build; then echo "build directory exists!"; fi
build directory exists!
# ... it is no longer necessary to specify the board:
$ west build --no-sysbuild -d ../build
```

Alternatively, we can use [West's build configuration options](https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html#configuration-options) to fix the board in the executing terminal. These options are similar to environment variables but are configuration options _only_ relevant to West. We can list the current West configuration options using `west config -l`:

```bash
$ west config -l
manifest.path=nrf
manifest.file=west.yml
zephyr.base=zephyr
```

The listed configuration options are part of [West's built-in configuration options](https://docs.zephyrproject.org/latest/develop/west/config.html#built-in-configuration-options) and come from the West workspace configuration. Since we're using a freestanding application, we'll ignore these options and focus on our build settings. We can add a default board configuration to our settings as follows:

```bash
$ west config build.board nrf52840dk/nrf52840
$ west config -l
manifest.path=nrf
manifest.file=west.yml
zephyr.base=zephyr
build.board=nrf52840dk/nrf52840
# It is also possible to delete an option
#, e.g., using `west config -d build.board`
```

> **Note:** The _West_ configuration options can also be used to define arguments for CMake. This can be useful when debugging or when defining your own CMake caches, refer to the [documentation](https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html#permanent-cmake-arguments) for details.

Now, we can run `west build` in our current terminal without specifying a board.

```bash
$ west build --no-sysbuild -d ../build
```

Notice that CMake does not pick up _West_'s configuration options, so executing `cmake -B ../build` would fail. One last parameter for `west build` that is worth mentioning is `--pristine`: Just like the `--pristine` option for `CMake`, instead of deleting the `build` folder, you can also use the `--pristine` to generate a new build:

```bash
$ west build --no-sysbuild -d ../build --pristine
```
