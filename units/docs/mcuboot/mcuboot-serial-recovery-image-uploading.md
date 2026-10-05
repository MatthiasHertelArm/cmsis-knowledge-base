---
id: "mcuboot-serial-recovery-image-uploading"
type: "concept"
domain: "boot-update"
title: "Serial recovery: Image uploading"
summary: "Uploading an image is targeted to the primary slot by default."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/serial_recovery.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/serial_recovery.md#image-uploading"
license: "Apache-2.0"
mode: "V"
---

Uploading an image is targeted to the primary slot by default.

An image can be loaded to other slots only when the ``MCUBOOT_SERIAL_DIRECT_IMAGE_UPLOAD`` option is enabled for the platform.

MCUboot supports progressive erasing of a slot to which an image is uploaded to if the ``MCUBOOT_ERASE_PROGRESSIVELY`` option is enabled.
As a result, a device can receive images smoothly, and can erase required part of a flash automatically.
