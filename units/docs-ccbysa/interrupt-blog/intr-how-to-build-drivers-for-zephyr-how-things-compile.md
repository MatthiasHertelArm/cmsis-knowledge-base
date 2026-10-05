---
id: "intr-how-to-build-drivers-for-zephyr-how-things-compile"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: How Things Compile"
summary: "One of the important things to know about driver development is how things compile. It may bend your mind a bit but we'll get through this together."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#how-things-compile"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of the important things to know about driver development is how things compile. It may bend your mind a bit but we'll get through this together.

### `CMakeLists.txt`

If you spend enough time in Zephyr, you may see some patterns emerge. Many folders and sub-folders have this dynamic duo: `CMakeLists.txt` and `Kconfig`. These files are where all the magic happens.

You may already have an idea of what `CMakeLists.txt` does by its name. It's a Makefile of sorts that you use to add source files and include folders to a project. The neat thing about `cmake` is that it's recursive (for better or for worse). This means a higher-level `CMakeLists.txt` file spells out what, if anything, can be found in subdirectories. There are no more ginormous Makefiles. You make the changes you need closest to the code that's affected.

For example, you can add subdirectories in `CMakeLists.txt` so they're part of the `cmake` path:

```cmake
# Point to NCS root directory.
set(NRF_DIR ${CMAKE_CURRENT_LIST_DIR} CACHE PATH "NCS root directory")

include(cmake/extensions.cmake)
include(cmake/multi_image.cmake)
include(cmake/reports.cmake)

zephyr_include_directories(include)

add_subdirectory(ext)
add_subdirectory(lib)
add_subdirectory(samples)
add_subdirectory(subsys)
add_subdirectory(drivers)
add_subdirectory(tests)
```

Sometimes they're used to set the directory as a project. This particular one is from the `https_client` example in nRF Connect SDK.

```cmake
cmake_minimum_required(VERSION 3.8.2)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(https_client)

target_sources(app PRIVATE src/main.c)
```

In my case, I'll show you how I used several `CMakeLists.txt` so the compiler knows about my device drivers!

### `Kconfig`

`Kconfig` allows you to create project-based configuration parameters. If you've ever used Nordic's Original SDK, you know the pain of their `sdk_config.h` file. *It's a nightmare.*

Like `CMakeLists.txt`, `Kconfig` files allow you to keep the configuration as close to your code. There's no massive top-level configuration manifest to be afraid of. You can add your code without breaking the repository. Good stuff, right?

Here's an example of a `Kconfig` from the `ncs/nrf/applications/asset_tracker` application

```
menu "Asset tracker"

rsource "src/ui/Kconfig"

config APPLICATION_WORKQUEUE_STACK_SIZE
    int "Application workqueue stack size"
    default 4096

config APPLICATION_WORKQUEUE_PRIORITY
    int "Application workqueue priority"
    default SYSTEM_WORKQUEUE_PRIORITY

menu "GPS"
...
```

You can see that it references separate `Kconfig` files as a dependency. You can also see that some environment variables are set with default values. You can either add them to your project's `prj.conf` *or* edit them using `west build -t menuconfig`. If you're looking to make permanent changes, you should use the `prj.conf` method.

The most important part about `Kconfig` files in regards to drivers is that you can use these variables as flags for conditional compilation.

As an example, here's what the `ncs/nrf/drivers/sensor/CMakeLists.txt` looks like:

```cmake
add_subdirectory_ifdef(CONFIG_BH1749 bh1749)
add_subdirectory_ifdef(CONFIG_SENSOR_SIM sensor_sim)
add_subdirectory_ifdef(CONFIG_PMW3360 pmw3360)
add_subdirectory_ifdef(CONFIG_PAW3212 paw3212)
```

You may notice that all the variables begin with `CONFIG_`. All variables produced by `Kconfig` have this prefix. So, for example, `APPLICATION_WORKQUEUE_STACK_SIZE` becomes `CONFIG_APPLICATION_WORKQUEUE_STACK_SIZE.`

In the `CMakeLists.txt` above, you can see that a subdirectory is only added if the driver is "enabled". `CONFIG_BH1749` happens to be the top-level environment variable to make that happen. You can also use this type of conditional compilation for your project code.

### `zephyr/module.yml`

`Kconfig` and `CMakeList.txt` are great, but where do we start? How does `west` know where to start looking for them?

The answer is a very unsuspecting file called `module.yml`. `module.yml` is usually found in the `/zephyr` subdirectory of a dependency. For example, here's the one for nRF Connect SDK located in `ncs/nrf/zephyr/`

Example

```
build:
  cmake: .
  kconfig: Kconfig.nrf
```

The file tells `west` where to find the appropriate base `Kconfig` and `CMakeLists.txt`. Those are the starting point for further repository traversal. Without these, there's no way to use your driver code in your application!
