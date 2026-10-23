---
id: "mcuboot-encrypted-images-rationale"
type: "concept"
domain: "boot-update"
title: "Encrypted images: Rationale"
summary: "To provide confidentiality of image data while in transport to the device or while residing on an external flash, MCUboot has support for encrypting/decrypting images on-the-fly while upgrading."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/encrypted_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/encrypted_images.md#rationale"
license: "Apache-2.0"
mode: "V"
---

To provide confidentiality of image data while in transport to the
device or while residing on an external flash, `MCUboot` has support
for encrypting/decrypting images on-the-fly while upgrading.

The image header needs to flag this image as `ENCRYPTED` (0x04) and
a TLV with the key must be present in the image. When upgrading the
image from the `secondary slot` to the `primary slot` it is automatically
decrypted (after validation). If swap upgrades are enabled, the image
located in the `primary slot`, also having the `ENCRYPTED` flag set and the
TLV present, is re-encrypted while swapping to the `secondary slot`.
