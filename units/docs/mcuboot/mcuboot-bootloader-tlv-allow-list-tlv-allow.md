---
id: "mcuboot-bootloader-tlv-allow-list-tlv-allow"
type: "concept"
domain: "boot-update"
title: "Bootloader: [TLV allow list](#tlv-allow)"
summary: "While reading unprotected TLVs from an image, MCUboot will try to match TLVs against list it has compiled in support for; each new defined TLV has to be added to that list, which is named allowed_unprot_tlvs and defined in image_validate.c."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#tlv-allow-list-tlv-allow"
license: "Apache-2.0"
mode: "V"
---

While reading unprotected TLVs from an image, MCUboot will try to match TLVs
against list it has compiled in support for; each new defined TLV has to be added
to that list, which is named `allowed_unprot_tlvs` and defined in
image_validate.c. The usage of the list is optional and can be controlled
during compilation with `MCUBOOT_USE_TLV_ALLOW_LIST` config identifier.
