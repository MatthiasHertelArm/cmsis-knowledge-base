---
id: "tfm-add-support-for-block-aligned-flas-current-implementation"
type: "concept"
domain: "security"
title: "Add support for block-aligned flash in Internal Trusted Storage: Current implementation"
summary: "In the current ITS filesystem design, each filesystem create or write operation requires two flash blocks to be updated: first the data block and then the metadata block. Buffering is avoided as much as possible to reduce RAM requirements."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_its_512_flash.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_512_flash.html#current-implementation"
license: "BSD-3-Clause"
mode: "V"
---

In the current ITS filesystem design, each filesystem create or write operation
requires two flash blocks to be updated: first the data block and then the
metadata block. Buffering is avoided as much as possible to reduce
RAM requirements.

However, if the ITS_FLASH_PROGRAM_UNIT is 512 Bytes then the data will have to
stored in a temporary memory location in order to be able to write
that much data in one-shot.
