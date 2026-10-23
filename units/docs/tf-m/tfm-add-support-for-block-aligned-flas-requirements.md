---
id: "tfm-add-support-for-block-aligned-flas-requirements"
type: "concept"
domain: "security"
title: "Add support for block-aligned flash in Internal Trusted Storage: Requirements"
summary: "Add support for block-aligned flash in Internal Trusted Storage: Requirements"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_its_512_flash.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_512_flash.html#requirements"
license: "BSD-3-Clause"
mode: "V"
---

- Allow page-aligned writes for up to 512 Bytes per page.
- Guarantee data integrity and power-failure reliability.
- Do not alter existing supported platform behaviour.
