---
id: "tfm-ff-m-isolation-mpu-region-access-permission"
type: "concept"
domain: "security"
title: "FF-M Isolation: Reference Implementation / MPU Region Access Permission"
summary: "The following content describes the memory access permission to represent the corresponding asset classes."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/ff_isolation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/ff_isolation.html#mpu-region-access-permission"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Reference Implementation_

The following content describes the memory access permission to represent the
corresponding asset classes.

These access permissions are available on Armv8-M MPU:

- Privileged Read-Only (RO)
- All RO
- Privileged Read-Write (RW)
- All RW
- Execute Never (XN)

And one more Armv8.1-M access permission:

- Privileged Execute Never (PXN)

The available regions type list:

======== =========== =============== ========================================
Type     Attributes  Privilege Level Asset
======== =========== =============== ========================================
P_RO     RO          Privileged      PRoT Code
P_ROXN   RO + XN     Privileged      PRoT Constant Data
P_RWXN   RW + XN     Privileged      PRoT Private Data/Peripheral
A_RO     RO          Any privilege   Partition/SPRTL Code
A_ROXN   RO + XN     Any privilege   Partition/SPRTL Constant Data
A_RWXN   RW + XN     Any privilege   Partition/SPRTL Private Data/Peripheral
A_ROPXN  RO + PXN    Any privilege   Armv8.1-M Partition Code
======== =========== =============== ========================================
