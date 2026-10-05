---
id: "mcuboot-encrypted-images-factory-programing-requirement"
type: "concept"
domain: "boot-update"
title: "Encrypted images: Factory-programing requirement"
summary: "It is important to have updates without any voids in encryption. Therefore, from the very beginning, flags and TLV's must be set accordingly. Perform the first flashing with an image signed by imgtool with encryption settings intended for DFU."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/encrypted_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md#factory-programing-requirement"
license: "Apache-2.0"
mode: "V"
---

It is important to have updates without any voids in encryption. 
Therefore, from the very beginning, flags and TLV's must be set accordingly.
Perform the first flashing with an image signed by imgtool with encryption settings
intended for DFU.
Append it with the `--clear` flag to keep the image unencrypted and ready for use.
