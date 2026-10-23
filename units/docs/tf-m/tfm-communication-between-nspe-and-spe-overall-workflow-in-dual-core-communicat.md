---
id: "tfm-communication-between-nspe-and-spe-overall-workflow-in-dual-core-communicat"
type: "concept"
domain: "security"
title: "Communication Between NSPE And SPE In Dual Core System: Overall workflow in dual-core communication"
summary: "The overall workflow in dual-core scenario can be described as follows"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/communication_between_nspe_and_spe_in_dual_core_systems.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/communication_between_nspe_and_spe_in_dual_core_systems.html#overall-workflow-in-dual-core-communication"
license: "BSD-3-Clause"
mode: "V"
---

The overall workflow in dual-core scenario can be described as follows

1. A non-secure application calls TF-M non-secure interface library to request
   Secure service. The TF-M non-secure interface library translates the Secure
   service into PSA Client calls.
2. TF-M non-secure interface library notifies TF-M of the PSA client call
   request, via mailbox. The HAL must define generic mailbox APIs to support
   various IPC implementations.
3. Inter-Processor Communication interrupt handler and mailbox handling in TF-M
   deal with the inbound mailbox event(s) and deliver the PSA client call
   request to TF-M SPM.
4. TF-M SPM processes the PSA client call request and dispatches it to the
   appropriate secure partition or handler.
5. After the PSA Client call is completed, the return value is sent back to NSPE
   via mailbox.
6. TF-M non-secure interface library fetches return value from mailbox.
7. The return value is returned to non-secure application.

The interfaces between NSPE app and TF-M NSPE interface library are unchanged
so the underlying platform specific details are transparent to NSPE
application.

Step 3-5 are covered in PSA client call handling flow in TF-M in detail.


**Note:** This document is partially complete since the introduction of the Hybrid Platform Scheduling support, which extends the operation of the mailbox communication between local and remote NSPEs with SPE described here. For more details see /design_docs/multi-cpu/hybrid_platform_solution.
