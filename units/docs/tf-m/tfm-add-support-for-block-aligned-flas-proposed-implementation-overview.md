---
id: "tfm-add-support-for-block-aligned-flas-proposed-implementation-overview"
type: "concept"
domain: "security"
title: "Add support for block-aligned flash in Internal Trusted Storage: Proposed implementation overview"
summary: "Add support for block-aligned flash in Internal Trusted Storage: Proposed implementation overview"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_its_512_flash.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_512_flash.html#proposed-implementation-overview"
license: "BSD-3-Clause"
mode: "V"
---

1. A new block-sized static buffer should be added to its_flash.c when
   `ITS_FLASH_PROGRAM_UNIT` is larger than currently supported.
2. Methods calling the flash API such as `its_flash_write()` or
   `its_flash_block_to_block_move()` will populate the buffer instead of
   directly programming the flash.
3. A new method `its_flash_flush()`, should be provided in order to flush
   the block buffer to the device.
4. `its_flash_flush()` should be called twice: Once after a data block
   update and once more after the metadata block update is completed.
5. The proposed design should require that the data block update is always
   completed before the metadata block update starts
6. Writes to the block buffer should be atomic, and guarded against corruption
   by data from different blocks.
