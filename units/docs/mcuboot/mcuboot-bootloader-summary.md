---
id: "mcuboot-bootloader-summary"
type: "concept"
domain: "boot-update"
title: "Bootloader: Summary"
summary: "The bootutil library performs most of the functions of a bootloader. In particular, the piece that is missing is the final step of actually jumping to the main image. This last step is instead implemented by the boot application."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#summary"
license: "Apache-2.0"
mode: "V"
---

MCUboot comprises two packages:

* The bootutil library (boot/bootutil)
* The boot application (each port has its own at boot/
)

The bootutil library performs most of the functions of a bootloader.  In
particular, the piece that is missing is the final step of actually jumping to
the main image.  This last step is instead implemented by the boot application.
Bootloader functionality is separated in this manner to enable unit testing of
the bootloader.  A library can be unit tested, but an application can't.
Therefore, functionality is delegated to the bootutil library when possible.
