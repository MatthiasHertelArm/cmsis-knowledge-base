---
id: "tfm-platform-documentation-example"
type: "concept"
domain: "security"
title: "Platform Documentation: Example"
summary: "Assuming a vendor ABCD123 wants to add and document a new platform Secure 1024 in TF-M. Here are the basic steps:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform/documenting_platform.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/documenting_platform.html#example"
license: "BSD-3-Clause"
mode: "V"
---

Assuming a vendor `ABCD123` wants to add and document a new platform
`Secure 1024` in TF-M. Here are the basic steps:

1. Create a folder `/docs/platform/ABCD123/`

2. Create a platform documentation under `/docs/platform/ABCD123`.
   A natural choice is to put a new platform under `/docs/platform/ABCD123/Secure_1024`
   folder but it's not required.

3. Create a file `/docs/platform/ABCD123/index.rst` with a platform entry, presuming
   it's location in `/docs/platform/ABCD123/Secure_1024/index.rst`:

```rst

#################
ABCD123 platforms
#################

.. toctree::
Secure 1024 <Secure_1024/index>
```
4. Finally, update `/docs/platform/index.rst` with a new vendor name:

```rst

##############
TF-M Platforms
##############

.. toctree::

    Arm <arm/index.rst>
    NXP <nxp/index.rst>
    Cypress <cypress/index.rst>
    ...
    ABCD123 <ABCD123/index.rst>
```
--------------

*Copyright (c) 2023, Arm Limited. All rights reserved.*
