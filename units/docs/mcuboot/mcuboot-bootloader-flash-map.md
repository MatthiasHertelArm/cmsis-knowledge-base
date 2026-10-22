---
id: "mcuboot-bootloader-flash-map"
type: "concept"
domain: "boot-update"
title: "Bootloader: Flash map"
summary: "A device's flash is partitioned according to its flash map. At a high level, the flash map maps numeric IDs to flash areas. A flash area is a region of disk with the following properties: 1."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/design.md#flash-map"
license: "Apache-2.0"
mode: "V"
---

A device's flash is partitioned according to its _flash map_.  At a high
level, the flash map maps numeric IDs to _flash areas_.  A flash area is a
region of disk with the following properties:
1. An area can be fully erased without affecting any other areas.
2. A write to one area does not restrict writes to other areas.

The bootloader uses the following flash area IDs:
```c
/* Independent from multiple image boot */
#define FLASH_AREA_BOOTLOADER         0
#define FLASH_AREA_IMAGE_SCRATCH      3
```
```c
/* If the bootloader is working with the first image */
#define FLASH_AREA_IMAGE_PRIMARY      1
#define FLASH_AREA_IMAGE_SECONDARY    2
```
```c
/* If the bootloader is working with the second image */
#define FLASH_AREA_IMAGE_PRIMARY      5
#define FLASH_AREA_IMAGE_SECONDARY    6
```

The bootloader area contains the bootloader image itself. The other areas are
described in subsequent sections. The flash could contain multiple executable
images therefore the flash area IDs of primary and secondary areas are mapped
based on the number of the active image (on which the bootloader is currently
working).
