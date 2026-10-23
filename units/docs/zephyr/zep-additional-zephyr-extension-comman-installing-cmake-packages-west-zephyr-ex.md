---
id: "zep-additional-zephyr-extension-comman-installing-cmake-packages-west-zephyr-ex"
type: "concept"
domain: "project"
title: "Additional Zephyr extension commands: Installing CMake packages: `west zephyr-export`"
summary: "This command registers the current Zephyr installation as a CMake config package in the CMake user package registry."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/zephyr-cmds.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/zephyr-cmds.rst"
license: "Apache-2.0"
mode: "V"
---

This command registers the current Zephyr installation as a CMake
config package in the CMake user package registry.

In Windows, the CMake user package registry is found in
`HKEY_CURRENT_USER\Software\Kitware\CMake\Packages`.

In Linux and MacOS, the CMake user package registry is found in.
`~/.cmake/packages`.

You may run this command when setting up a Zephyr workspace. If you do,
application CMakeLists.txt files that are outside of your workspace will be
able to find the Zephyr repository with the following:

```cmake

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
```
See `share/zephyr-package/cmake` for details.
