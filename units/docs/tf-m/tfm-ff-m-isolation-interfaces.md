---
id: "tfm-ff-m-isolation-interfaces"
type: "concept"
domain: "security"
title: "FF-M Isolation: Reference Implementation / Interfaces"
summary: "The isolation implementation is based on the HAL framework. The SPM relies on the HAL API to perform the necessary isolation related operations."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/ff_isolation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/ff_isolation.html#interfaces"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Reference Implementation_

The isolation implementation is based on the HAL framework. The SPM relies on
the HAL API to perform the necessary isolation related operations.

The requirement the software need to do are these:

- Create enough isolation protection at the early stage of system booting, just
  need to focus on the SPM domain.
- Create an isolation domain between secure and non-secure before the jump to
  the non-secure world.
- Create an isolation domain for each Secure Partition after the Secure
  Partition is loaded and before jumping to its entry point. The isolation
  domain should cover all the assets of the Secure Partition, include all its
  memory, interrupts, and peripherals.
- Switch isolation domains when scheduling different Secure Partitions.
- It is also a requirement that the platform needs to help to check if the
  caller of the PSA APIs is permitted to access some memory ranges.

The design document
TF-M Hardware Abstraction Layer
gives a detail design, include the platform initialization, isolation
interfaces. Please refer to it for more detail.
