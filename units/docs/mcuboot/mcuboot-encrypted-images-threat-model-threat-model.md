---
id: "mcuboot-encrypted-images-threat-model-threat-model"
type: "concept"
domain: "boot-update"
title: "Encrypted images: [Threat model](#threat-model)"
summary: "The encrypted image support is supposed to allow for confidentiality if the image is not residing on the device or is written to external storage, eg a SPI flash being used for the secondary slot."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/encrypted_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md#threat-model-threat-model"
license: "Apache-2.0"
mode: "V"
---

The encrypted image support is supposed to allow for confidentiality
if the image is not residing on the device or is written to external
storage, eg a SPI flash being used for the secondary slot.

It does not protect against the possibility of attaching a JTAG and
reading the internal flash memory, or using some attack vector that
enables dumping the internal flash in any way.

Since decrypting requires a private key (or secret if using symmetric
crypto) to reside inside the device, it is the responsibility of the
device manufacturer to guarantee that this key is already in the device
and not possible to extract.
