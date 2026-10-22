---
id: "tfm-memory-mapped-iovecs-introduction"
type: "concept"
domain: "security"
title: "Memory-mapped IOVECs: Introduction"
summary: "FF-M v1.1 introduced MM-IOVEC functionality. Its initial implementation in TF-M restricted the capability to isolation level 1. The build system displays a warning banner when MM-IOVEC is enabled."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/mm_iovec.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/mm_iovec.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

Key terms:

* **IL1**: Lowest isolation level

* **IL2 / IL3**: Higher isolation levels

* **SSM** - Secure Shared Memory: refers to a block of secure memory that is
  available to RoTs but is not private to any single RoT.


FF-M v1.1 introduced MM-IOVEC functionality.
Its initial implementation in TF-M restricted the capability to isolation
level 1.
The build system displays a warning banner when MM-IOVEC is enabled.
