---
id: "tfm-ff-m-isolation-example-image-layout"
type: "concept"
domain: "security"
title: "FF-M Isolation: Reference Implementation / Example Image Layout"
summary: "The secure firmware image contains components such as partitions, SPM and the shared code and data. Each component may have different class assets."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/ff_isolation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/ff_isolation.html#example-image-layout"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Reference Implementation_

The secure firmware image contains components such as partitions, SPM and the
shared code and data. Each component may have different class assets. There
would be advantages if placing the assets from all components with the same
access attributes into one same region:

- The data relocating or clearing when booting can be done in one step instead
  of breaking into fragments.
- Assets with statically assigned access attribute can share the same MPU
  region which saves regions.

Take the TF-M existing implementation image layout as an example::
```
 Level 1      Level 2             Level 3
 Boundaries   Boundaries          Boundaries
+------------+----------+------------------------------------+
|            |          |    PRoT SPM                Code    |
|            | PRoT     +------------------------------------+
|            | Code     |    PRoT Service            Code    |
|  Code      +----------+------------------------------------+
|  (ROM)     |          |    Partition 1             Code    |
|            |          +------------------------------------+
|            | ARoT     |    Partition N             Code    |
|            | Code     +------------------------------------+
|            |          |    SPRTL                   Code    |
+------------+----------+------------------------------------+
Check [4] for more details between Code and Constant Data.
+------------+----------+------------------------------------+
|            | PRoT     |    PRoT SPM       Constant Data    |
|            | Constant +------------------------------------+
|            | Data     |    PRoT Service   Constant Data    |
|  Constant  +----------+------------------------------------+
|   Data     | ARoT     |    Partition 1    Constant Data    |
|   (ROM)    | Constant +------------------------------------+
|            | Data     |    Partition N    Constant Data    |
|            |          +------------------------------------+
|            |          |    SPRTL          Constant Data    |
+------------+----------+------------------------------------+

+------------+----------+------------------------------------+
|            | PRoT     |    PRoT SPM        Private Data    |
|            | Private  +------------------------------------+
|            | Data     |    PRoT Service    Private Data    |
|  Private   +----------+------------------------------------+
|   Data     |          |    Partition 1     Private Data    |
|   (RAM)    | ARoT     +------------------------------------+
|            | Private  |    Partition N     Private Data    |
|            | Data     +------------------------------------+
|            |          |    SPRTL           Private Data    |
+------------+----------+------------------------------------+
```

**Note:** 1. Multiple binaries image implementation could also reference this layout if its hardware protection unit can cover the exact boundaries mentioned above. 2. Private data includes both initialized and zero-initialized (ZI) sections. Check chapter `3.1.1` of FF-M [1]_ for the details. 3. This diagram shows the boundaries but not orders. The order of regions inside one upper region can be adjusted freely. 4. As described in the `important` of Memory Asset Class, the setting between Code and Constant Data can be skipped if the executable access method is not applied to constant data. In this case, the groups of Code and Constant Data can be combined or even mixed -- but the boundary between PRoT and ARoT are still required under level higher than 1.
