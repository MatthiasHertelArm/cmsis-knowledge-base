---
id: "mcuboot-encrypted-images-upgrade-process-upgrade-process"
type: "concept"
domain: "boot-update"
title: "Encrypted images: [Upgrade process](#upgrade-process)"
summary: "When starting a new upgrade process, MCUboot checks that the image in the secondary slot has the ENCRYPTED flag set and has the required TLV with the encrypted key."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/encrypted_images.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/encrypted_images.md#upgrade-process-upgrade-process"
license: "Apache-2.0"
mode: "V"
---

When starting a new upgrade process, `MCUboot` checks that the image in the
`secondary slot` has the `ENCRYPTED` flag set and has the required TLV with the
encrypted key. It then uses its internal private/secret key to decrypt
the TLV containing the key. Given that no errors are found, it will then
start the validation process, decrypting the blocks before check. A good
image being determined, the upgrade consists in reading the blocks from
the `secondary slot`, decrypting and writing to the `primary slot`.

If swap using scratch is used for the upgrade process, the decryption happens
when copying the content of the scratch area to the `primary slot`, which means
the scratch area does not contain the image unencrypted. However, unless
`MCUBOOT_SWAP_SAVE_ENCTLV` is enabled, the decryption keys are stored in
plaintext in the scratch area. Therefore, `MCUBOOT_SWAP_SAVE_ENCTLV` must be
enabled if the scratch area does not reside in the internal flash memory of the
MCU, to avoid attacks that could interrupt the upgrade and read the plaintext
decryption keys from external flash memory.

Also when swap is used, the image in the `primary slot` is checked for
presence of the `ENCRYPTED` flag and the key TLV. If those are present the
sectors are re-encrypted when copying from the `primary slot` to
the `secondary slot`.

---
***Note***

*Each encrypted image must have its own key TLV that should be unique*
*and used only for this particular image.*

---

Also when swap method is employed, the sizes of both images are saved to
the status area just before starting the upgrade process, because it
would be very hard to determine this information when an interruption
occurs and the information is spread across multiple areas.
