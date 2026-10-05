---
id: "intr-how-to-build-drivers-for-zephyr-full-example"
type: "concept"
domain: "debug"
title: "How to Build Drivers for Zephyr: Full Example"
summary: "Below are all of the KConfig and CMakeLists.txt files that are part of my project, along with their relative project path."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-23-building-drivers-on-zephyr.md"
doc_source: "https://interrupt.memfault.com/blog/building-drivers-on-zephyr#full-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Below are all of the `KConfig` and `CMakeLists.txt` files that are part of my project, along with their relative project path.

**`ncs/pyrinas/CMakeLists.txt`**

```cmake
#
# Copyright (c) 2020 Circuit Dojo
#
# SPDX-License-Identifier: Apache-2.0
#

# Point to Pyrinas root directory.
set(PYRINAS_DIR ${CMAKE_CURRENT_LIST_DIR} CACHE PATH "Pyrinas root directory")

zephyr_include_directories(include)

add_subdirectory(lib)
add_subdirectory(ext)
add_subdirectory(drivers)
```

**`ncs/pyrinas/drivers/CMakeLists.txt`**

```cmake
#
# Copyright (c) 2020 Circuit Dojo LLC
#
# SPDX-License-Identifier: Apache-2.0
#

add_subdirectory(rtc)
```

**`ncs/pyrinas/drivers/rtc/CMakeLists.txt`**

```cmake
add_subdirectory_ifdef(CONFIG_PCF85063A		pcf85063a)
```

**`ncs/pyrinas/drivers/rtc/pcf86063a/CMakeLists.txt`**

```cmake
zephyr_library()

zephyr_library_sources_ifdef(CONFIG_PCF85063A pcf85063a.c)
```

The `Kconfig` files follow a very similar pattern. You can use the same pattern for your projects as well.

**`ncs/pyrinas/Kconfig.pyrinas`**

```
menu "Pyrinas"

rsource "lib/Kconfig"
rsource "drivers/Kconfig"

endmenu
```

*Side note:* The `Kconfig` in a module's root doesn't need a suffix. I chose to add `.pyrinas` to be consistent with the nRF Connect Studio and Zephyr repo. Make sure whatever you use is reflected in `zephyr/module.yml`.

**`ncs/pyrinas/drivers/Kconfig`**

```
comment "Device Drivers"

rsource "rtc/Kconfig"
```

**`ncs/pyrinas/drivers/rtc/Kconfig`**

```
comment "RTC Drivers"

rsource "pcf85063a/Kconfig"
```

**`ncs/pyrinas/drivers/rtc/pcf85063a/Kconfig`**

```
# PCF85063A Nano Power Real time Clock configuration options

menuconfig PCF85063A
    bool "PCF85063A Three Axis Accelerometer"
    depends on (I2C && HAS_DTS_I2C)
    help
      Enable SPI/I2C-based driver for PCF85063A based RTC
```

As you can imagine, it's more complicated when your drivers are many levels deep. In any case, the above example should give you an idea of how to organize your `Kconfig` and `CMakeLists.txt`.
