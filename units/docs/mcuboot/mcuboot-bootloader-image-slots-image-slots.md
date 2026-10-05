---
id: "mcuboot-bootloader-image-slots-image-slots"
type: "concept"
domain: "boot-update"
title: "Bootloader: [Image slots](#image-slots)"
summary: "A portion of the flash memory can be partitioned into multiple image areas, each contains two image slots: a primary slot and a secondary slot."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#image-slots-image-slots"
license: "Apache-2.0"
mode: "V"
---

A portion of the flash memory can be partitioned into multiple image areas, each
contains two image slots: a primary slot and a secondary slot.
Normally, the bootloader will only run an image from the primary slot, so
images must be built such that they can run from that fixed location in flash
(the exception to this is the [direct-xip](#direct-xip) and the
[ram-load](#ram-load) upgrade mode). If the bootloader needs to run the
image resident in the secondary slot, it must copy its contents into the primary
slot before doing so, either by swapping the two images or by overwriting the
contents of the primary slot. The bootloader supports either swap- or
overwrite-based image upgrades, but must be configured at build time to choose
one of these two strategies.
