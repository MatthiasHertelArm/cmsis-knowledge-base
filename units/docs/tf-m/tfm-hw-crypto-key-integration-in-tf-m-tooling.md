---
id: "tfm-hw-crypto-key-integration-in-tf-m-tooling"
type: "concept"
domain: "security"
title: "HW crypto key integration in TF-M secure boot: Tooling"
summary: "bl2/ext/mcuboot/scripts/imgtool.py will be modified to include the whole public key to the TLV area (instead of the hash)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/secure_boot_hw_key_integration.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_hw_key_integration.html#tooling"
license: "BSD-3-Clause"
mode: "V"
---

`bl2/ext/mcuboot/scripts/imgtool.py` will be modified to include the whole
public key to the TLV area (instead of the hash).

Table to compare the current and proposed solution::
```
|---------|-----------------------|-------------------|--------------------|
|         |Key format in manifest |Key in MCUBoot code|     Key in HW      |
|---------|-----------------------|-------------------|--------------------|
|Proposed |    Full public key    |  No key embedded  | Hash of public key |
|---------|-----------------------|-------------------|--------------------|
|Current  |   Hash of public key  |  Full public key  |   No key in HW     |
|---------|-----------------------|-------------------|--------------------|
```
--------------

*Copyright (c) 2019, Arm Limited. All rights reserved.*
