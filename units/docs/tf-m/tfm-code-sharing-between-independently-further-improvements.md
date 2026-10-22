---
id: "tfm-code-sharing-between-independently-further-improvements"
type: "concept"
domain: "security"
title: "Code sharing between independently linked XIP binaries: Further improvements"
summary: "This design focuses only on sharing the cryptography code. However, other code could be shared as well. Some possibilities:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/code_sharing.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/code_sharing.html#further-improvements"
license: "BSD-3-Clause"
mode: "V"
---

This design focuses only on sharing the cryptography code. However, other code
could be shared as well. Some possibilities:

- Flash driver
- Serial driver
- Image metadata parsing code
- etc.

--------------

*Copyright (c) 2020-2024, Arm Limited. All rights reserved.*
