---
id: "mcuboot-bootloader-integrity-check"
type: "concept"
domain: "boot-update"
title: "Bootloader: Integrity check"
summary: "An image is checked for integrity immediately before it gets copied into the primary slot."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#integrity-check"
license: "Apache-2.0"
mode: "V"
---

An image is checked for integrity immediately before it gets copied into the
primary slot.  If the bootloader doesn't perform an image swap, then it can
perform an optional integrity check of the image in the primary slot if
`MCUBOOT_VALIDATE_PRIMARY_SLOT` is set, otherwise it doesn't perform an
integrity check.

During the integrity check, the bootloader verifies the following aspects of
an image:

  * 32-bit magic number must be correct (`IMAGE_MAGIC`).
  * Image must contain an `image_tlv_info` struct, identified by its magic
    (`IMAGE_TLV_PROT_INFO_MAGIC` or `IMAGE_TLV_INFO_MAGIC`) exactly following
    the firmware (`hdr_size` + `img_size`). If `IMAGE_TLV_PROT_INFO_MAGIC` is
    found then after `ih_protect_tlv_size` bytes, another `image_tlv_info`
    with magic equal to `IMAGE_TLV_INFO_MAGIC` must be present.
  * Image must contain a SHA256 TLV.
  * Calculated SHA256 must match SHA256 TLV contents.
  * Image *may* contain a signature TLV.  If it does, it must also have a
    KEYHASH TLV with the hash of the key that was used to sign. The list of
    keys will then be iterated over looking for the matching key, which then
    will then be used to verify the image contents.

For low performance MCU's where the validation is a heavy process at boot
(~1-2 seconds on a arm-cortex-M0), the `MCUBOOT_VALIDATE_PRIMARY_SLOT_ONCE`
could be used. This option will cache the validation result as described above
into the magic area of the primary slot. The next boot, the validation will be
skipped if the previous validation was succesfull. This option is reducing the
security level since if an attacker could modify the contents of the flash after
a good image has been validated, the attacker could run his own image without
running validation again. Enabling this option should be done with care.
