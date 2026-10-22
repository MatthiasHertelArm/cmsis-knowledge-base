---
id: "tfm-add-support-for-block-aligned-flas-considerations"
type: "concept"
domain: "security"
title: "Add support for block-aligned flash in Internal Trusted Storage: Considerations"
summary: "For example, if a board powers down through a 512 page program operation, the next read operation should return an error rather than read invalid data."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_its_512_flash.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_512_flash.html#considerations"
license: "BSD-3-Clause"
mode: "V"
---

- The proposed implementation will increase the RAM usage of ITS by the size
  of a block, only for platforms which require block-aligned writes.
- Currently power-failure is detected by software by incrementing an 8-bit
  metadata header field (`swap_count`), as the last written byte. When the
  proposed block-buffer is used, the block is programmed in one-shot and the
  order the bytes are written on the physical device, is hardware dependent.
- A set of guarantees are required by the supported flash ECC devices.
  The device's flash APIs should provide a mechanism to capture and raise
  incomplete program operations, as well as write bytes in a sequential order.

For example, if a board powers down through a 512 page program operation, the
next read operation should return an error rather than read invalid data.
