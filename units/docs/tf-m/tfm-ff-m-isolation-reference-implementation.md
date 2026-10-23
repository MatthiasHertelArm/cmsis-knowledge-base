---
id: "tfm-ff-m-isolation-reference-implementation"
type: "concept"
domain: "security"
title: "FF-M Isolation: Reference Implementation"
summary: "This chapter describes the isolation implementation inside SPE by using the Armv8-M architecture component - Memory Protection Unit (MPU). The MPU can isolate CPU execution and data access."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/ff_isolation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/ff_isolation.html#reference-implementation"
license: "BSD-3-Clause"
mode: "V"
---

This chapter describes the isolation implementation inside SPE by using the
Armv8-M architecture component - Memory Protection Unit (MPU). The MPU can
isolate CPU execution and data access.


**Note:** Previous version M-profile architecture MPU setting is similar in concept but the difference in practical register formats, which is not described in this document.

The MPU protects memory assets by regions. Each region represents a memory
range with specific access attributes.


**Note:** The maximum numbers of MPU regions are platform-specific.

The SPM is running under the privileged mode for handling access from services.
The MPU region for SPM needs to be available all the time since SPM controls
the MPU setting while scheduling.

Since partitions are scheduled by SPM, the MPU regions corresponding to the
partitions can be configured dynamically while scheduling. Since there is only
one running at a time and all others are deactivated, the SPM needs to set up
necessary regions for each asset type in one partition only.

There is reusable code like the C-Runtime and RoT Service API which are same
across different partitions. TF-M creates a Secure Partition Runtime Library
(SPRTL) as a specific library shared by the Secure Partition. Please refer to
Secure Partition Runtime Library
for more detail.


**Note:** Enable SPRTL makes it hard to comply with the rules I4, I5 and I6, duplicating the library code can be one solution but it is not "shared" library anymore.

As mentioned in the last chapter, MMIO needs extra MPU regions as private data.
