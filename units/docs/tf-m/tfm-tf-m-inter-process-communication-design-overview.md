---
id: "tfm-tf-m-inter-process-communication-design-overview"
type: "concept"
domain: "security"
title: "TF-M Inter-Process Communication: Design Overview"
summary: "TF-M Inter-Process Communication: Design Overview"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_psa_inter_process_communication.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_psa_inter_process_communication.html#design-overview"
license: "BSD-3-Clause"
mode: "V"
---

Components for implementing IPC:

- SPM – for partition information and isolation actions
- Core – for exception handling
- Memory pool
- Message manager
- Thread
- Synchronization objects
- PSA API
