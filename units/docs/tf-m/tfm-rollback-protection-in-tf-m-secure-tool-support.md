---
id: "tfm-rollback-protection-in-tf-m-secure-tool-support"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: Tool support"
summary: "There is a Python script, imgtool.py which is used to prepare the new image for upgrade (add header, sign the image, append TLV section)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#tool-support"
license: "BSD-3-Clause"
mode: "V"
---

There is a Python script, `imgtool.py` which is used to prepare the new image
for upgrade (add header, sign the image, append TLV section). This script must
be modified to get an additional command line argument which serves as security
counter. The security counter must be included in the integrity protected part
of the TLV section.

--------------

*Copyright (c) 2019-2020, Arm Limited. All rights reserved.*
