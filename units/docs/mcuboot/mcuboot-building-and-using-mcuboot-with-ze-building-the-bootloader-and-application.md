---
id: "mcuboot-building-and-using-mcuboot-with-ze-building-the-bootloader-and-application"
type: "concept"
domain: "boot-update"
title: "Building and using MCUboot with Zephyr: Building the bootloader and application together (sysbuild)"
summary: "Sysbuild is a CMake project in zephyr which allows for building multiple Zephyr images as part of a single build."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/readme-zephyr.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/readme-zephyr.md#building-the-bootloader-and-application-together-sysbuild"
license: "Apache-2.0"
mode: "V"
---

Sysbuild is a CMake project in zephyr which allows for building multiple Zephyr
images as part of a single build. It has configuration for the sysbuild image
itself which can be used to build other images or set configuration, including
MCUboot configuration. To enable MCUboot support in a project, one simply needs
to enable the ``SB_CONFIG_BOOTLOADER_MCUBOOT`` sysbuild Kconfig, as an example
using hello world, `samples/hello_world` in the Zephyr tree:

```
  cd samples/hello_world
  west build -b <board> --sysbuild -- -DSB_CONFIG_BOOTLOADER_MCUBOOT=y
```

This will build MCUboot and hello world, including enabling the MCUboot Kconfigs
in the hello world application to allow MCUboot to build it. Sysbuild is the
recommended way of building an application with MCUboot support in Zephyr,
though MCUboot itself (and the application) can also be built manually, as
described below.

See the `share/sysbuild/images/bootloader/Kconfig` file in the Zephyr tree for
sysbuild Kconfig options that can be used to configure MCUboot in a project,
including mode of MCUboot, the signing/encryption keys and other options. These
options will be propagated to both MCUboot and the application by sysbuild
automatically.
