---
id: "mcuboot-porting-how-to-configuration-file"
type: "concept"
domain: "boot-update"
title: "Porting how-to: Configuration file"
summary: "You must provide a file, mcuboot_config/mcuboot_config.h. This is included by several files in the \"library\" portion of MCUboot; it provides preprocessor definitions that configure the library's build."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/PORTING.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/PORTING.md#configuration-file"
license: "Apache-2.0"
mode: "V"
---

You must provide a file, mcuboot_config/mcuboot_config.h. This is
included by several files in the "library" portion of MCUboot; it
provides preprocessor definitions that configure the library's
build.

See the file samples/mcuboot_config/mcuboot_config.template.h for a
starting point and more information. This is a good place to convert
settings in your environment's configuration system to those required
by MCUboot. For example, Mynewt uses MYNEWT_VAL() and Zephyr uses
Kconfig; these configuration systems are converted to MCUBOOT_ options
in the following files:

- boot/zephyr/include/mcuboot_config/mcuboot_config.h
- boot/mynewt/mcuboot_config/include/mcuboot_config/mcuboot_config.h
