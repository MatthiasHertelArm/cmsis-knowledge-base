---
id: "mcuboot-porting-how-to"
type: "concept"
domain: "boot-update"
title: "Porting how-to"
summary: "This document describes the requirements and necessary steps required to port MCUboot to a new target OS."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/PORTING.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/PORTING.md"
license: "Apache-2.0"
mode: "V"
---

This document describes the requirements and necessary steps required to port
`MCUboot` to a new target `OS`.

# Requirements

* `MCUboot` requires a configuration file, which can be included as
   mcuboot_config/mcuboot_config.h, which configures various options
   (that begin with MCUBOOT_).

* `MCUboot` requires that the target provides a `flash` API with ability to
  get the flash's minimum write size, and read/write/erase individual sectors.

* `MCUboot` doesn't bundle a cryptographic library, which means the target
  OS must already have it bundled. The supported libraries at the moment are
  either `Mbed TLS` or the set `tinycrypt` + `Mbed TLS` (where `Mbed TLS` is
  used to provide functionality not existing in `tinycrypt`).

# Steps to port
