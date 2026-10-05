---
id: "tfm-spm-backends-implementation-recommendations"
type: "concept"
domain: "security"
title: "SPM Backends: Implementation Recommendations"
summary: "If an implementation doesn't contain any IPC model Secure Partition and only requires isolation level 1, then it is recommended to select the SFN backend to optimize memory consumption and execution performance."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/spm_backends.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/spm_backends.html#implementation-recommendations"
license: "BSD-3-Clause"
mode: "V"
---

If an implementation doesn't contain any IPC model Secure Partition and only
requires isolation level 1, then it is recommended to select the SFN backend
to optimize memory consumption and execution performance.

If an implementation contains any IPC model Secure Partition or requires
isolation level 2 or 3, then the IPC backend is required.
