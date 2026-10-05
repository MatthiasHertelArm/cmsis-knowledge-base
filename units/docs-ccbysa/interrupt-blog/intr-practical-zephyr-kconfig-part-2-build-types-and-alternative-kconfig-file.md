---
id: "intr-practical-zephyr-kconfig-part-2-build-types-and-alternative-kconfig-file"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Kconfig (Part 2): Using different configuration files / Build types and alternative Kconfig files"
summary: "Part of: Using different configuration files"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-01-24-practical_zephyr_kconfig.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_kconfig#build-types-and-alternative-kconfig-files"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Using different configuration files_

Zephyr doesn't use pre-defined build types such as _Debug_ or _Release_ builds. It is up to the application to decide the optimization options and build types. Different build types in Zephyr are supported using [alternative `Kconfig` files](https://docs.zephyrproject.org/latest/develop/application/index.html#basics), specified using the [`CONF_FILE`](https://docs.zephyrproject.org/latest/develop/application/index.html#important-build-system-variables) build system variable.

Let's freshen up on the _build system variables_: These variables are _not_ direct parameters for the build and configuration systems used by Zephyr, e.g., the `--build-dir` option for `west build`, but are available globally. As described in the [official documentation on important build system variables](https://docs.zephyrproject.org/latest/develop/application/index.html#important-build-system-variables), there are multiple ways to pass such variables to the build system. We'll repeat two of the available options here:

1. A build system variable may exist as an environment variable.
2. A build system variable may be passed to `west build` as [a one-time CMake argument](https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html#one-time-cmake-arguments) after a double dash `--`.

We'll stick to the second option and use a [one-time CMake argument](https://docs.zephyrproject.org/latest/develop/west/build-flash-debug.html#one-time-cmake-arguments), as shown in the [application development basics in the official documentation](https://docs.zephyrproject.org/latest/develop/application/index.html#basics). First, let's go ahead and create a [`prj_release.conf`](https://github.com/lmapii/practical-zephyr/blob/main/01_kconfig/prj_release.conf), which defines our symbols for the `release` build type:

```
$ tree --charset=utf-8 --dirsfirst
.
├── src
│   └── main.c
├── CMakeLists.txt
├── prj.conf
└── prj_release.conf

$ cat prj_release.conf
```

```conf
CONFIG_LOG=n
CONFIG_PRINTK=n
CONFIG_BOOT_BANNER=n
CONFIG_EARLY_CONSOLE=n
CONFIG_OVERRIDE_FRAME_POINTER_DEFAULT=y
CONFIG_USE_SEGGER_RTT=n
CONFIG_BUILD_OUTPUT_STRIPPED=y
CONFIG_FAULT_DUMP=0
CONFIG_STACK_SENTINEL=y

# Optimize build for size
CONFIG_SIZE_OPTIMIZATIONS=y
```

For our release build, we set the symbol `CONFIG_SIZE_OPTIMIZATIONS` to `y` and thereby optimize our release build for _size_: [Build optimizations](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPILER_OPTIMIZATIONS) are not set up in your _CMake_ configuration, but instead using _Kconfig_. Don't worry about all the other symbols in this file for now. We'll catch up on them in the section about [Kconfig hardening](#kconfig-hardening).

We can now instruct _West_ to use this `prj_release.conf` _instead_ of our `prj.conf` for the build by using the following command:

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 -d ../build -- -DCONF_FILE=prj_release.conf
```

If you scroll through the output of the `west build` command, you'll notice that _Kconfig_ merged `prj_release.conf` into our final configuration:

```
Parsing /opt/nordic/ncs/v3.2.1/zephyr/Kconfig
Loaded configuration '/opt/nordic/ncs/v3.2.1/zephyr/boards/nordic/nrf52840dk/nrf52840dk_nrf52840_defconfig'
Merged configuration '/path/to/01_kconfig/prj_release.conf'
Configuration saved to '/path/to/zephyr_practical/build/zephyr/.config'
```

Thus, in short, Zephyr accepts build types by specifying an alternative `Kconfig` file that typically uses the file name format `prj_<build>.conf`, using the `CONF_FILE` build system variable. The name of the build type is entirely application-specific and does not imply any, e.g., compiler optimizations.

> **Notice:** Zephyr uses _Kconfig_ to specify build types and also optimizations. Thus, _CMake_ options such as [`CMAKE_BUILD_TYPE`](https://cmake.org/cmake/help/latest/variable/CMAKE_BUILD_TYPE.html) are typically **not** used directly in Zephyr projects. This includes compiler optimization flags such as `-Os` or `-O2`, which are set using the [`CONFIG_COMPILER_OPTIMIZATIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COMPILER_OPTIMIZATIONS) in Kconfig instead.
