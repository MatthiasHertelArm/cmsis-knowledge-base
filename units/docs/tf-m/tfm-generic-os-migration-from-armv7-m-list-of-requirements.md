---
id: "tfm-generic-os-migration-from-armv7-m-list-of-requirements"
type: "concept"
domain: "security"
title: "Generic OS migration from Armv7-M to Armv8-M architecture: List of requirements"
summary: "Generic OS migration from Armv7-M to Armv8-M architecture: List of requirements"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/os_migration_guide_armv8m.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/os_migration_guide_armv8m.html#list-of-requirements"
license: "BSD-3-Clause"
mode: "V"
---

- If the same OS codebase is used for both Secure and Non Secure builds, it is
  suggested to put specific code targeted to the Non Secure build under a
  compile time switch, e.g. `#if (DOMAIN_NS == 1U)`. The OS build system in
  this case needs to be amended accordingly to support this new switch.
- If the OS implements stack limit checking, the `PSPLIM` register
  needs to be initialized and properly handled during thread context switch
  operations.
- If the OS manipulates directly the Link Register, the default Link Register
  value used in Handler mode transitions needs to be differentiated between
  Secure and Non Secure builds, i.e. `0xFD` and `0xBC`, respectively.
- If the OS manages the non-secure client identification, please check the
  Non-secure Client Extension Integration Guide.

--------------

*Copyright (c) 2018-2021, Arm Limited. All rights reserved.*
