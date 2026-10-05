---
id: "mcuboot-bootloader-protected-tlvs-protected-tlvs"
type: "concept"
domain: "boot-update"
title: "Bootloader: [Protected TLVs](#protected-tlvs)"
summary: "If the TLV area contains protected TLV entries, by beginning with a struct image_tlv_info with a magic value of IMAGE_TLV_PROT_INFO_MAGIC then the data of those TLVs must also be integrity and authenticity protected."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/design.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/design.md#protected-tlvs-protected-tlvs"
license: "Apache-2.0"
mode: "V"
---

If the TLV area contains protected TLV entries, by beginning with a `struct
image_tlv_info` with a magic value of `IMAGE_TLV_PROT_INFO_MAGIC` then the
data of those TLVs must also be integrity and authenticity protected. Beyond
the full size of the protected TLVs being stored in the `image_tlv_info`,
the size of the protected TLVs together with the size of the `image_tlv_info`
struct itself are also saved in the `ih_protected_size` field inside the
header.

Whenever an image has protected TLVs the SHA256 has to be calculated over
not just the image header and the image but also the TLV info header and the
protected TLVs.

```
A +---------------------+
  | Header              | <- struct image_header
  +---------------------+
  | Payload             |
  +---------------------+
  | TLV area            |
  | +-----------------+ |    struct image_tlv_info with
  | | TLV area header | | <- IMAGE_TLV_PROT_INFO_MAGIC (optional)
  | +-----------------+ |
  | | Protected TLVs  | | <- Protected TLVs (struct image_tlv)
B | +-----------------+ |
  | | TLV area header | | <- struct image_tlv_info with IMAGE_TLV_INFO_MAGIC
C | +-----------------+ |
  | | SHA256 hash     | | <- hash from A - B (struct image_tlv)
D | +-----------------+ |
  | | Keyhash         | | <- indicates which pub. key for sig (struct image_tlv)
  | +-----------------+ |
  | | Signature       | | <- signature from C - D (struct image_tlv), only hash
  | +-----------------+ |
  +---------------------+
```
