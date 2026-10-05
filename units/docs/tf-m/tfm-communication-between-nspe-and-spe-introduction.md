---
id: "tfm-communication-between-nspe-and-spe-introduction"
type: "concept"
domain: "security"
title: "Communication Between NSPE And SPE In Dual Core System: Introduction"
summary: "This document describes the communication design between the Non-secure Processing Environment (NSPE) and Secure Processing Environment (SPE) in TF-M on a dual-core system."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/multi-cpu/communication_between_nspe_and_spe_in_dual_core_systems.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/communication_between_nspe_and_spe_in_dual_core_systems.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

This document describes the communication design between the Non-secure
Processing Environment (NSPE) and Secure Processing Environment (SPE) in TF-M on
a dual-core system.

The dual-core system has the following characteristics:

- NSPE and SPE are properly isolated and protected following PSA specification.
- An Arm M-profile core hosts SPE and acts as the Secure core.
- Another core hosts NSPE and runs non-secure applications.
- An Inter-Processor Communication hardware module is available in the system
  for communication between NSPE core and SPE core.
- TF-M runs on the Secure core with platform-specific drivers support.


**Note:** All the concepts for dual-cpu can be extended to multi-cpu without loss of generality. Also see the Hybrid Platform section for further details.


### Scope


This design document focuses on the dual-core communication design inside TF-M.
Some changes to TF-M core and Secure Partition Manager (SPM) are listed to
support the dual-core communication. This document only discusses the
implementation in TF-M Inter-Process Communication (IPC) model.
The TF-M non-secure interface library depends on the mailbox and NS real-time
operating system (RTOS) implementations. These components are not described in
detail.

This document defines the requirements for mailbox functionality. For detailed
mailbox design, see the dedicated mailbox document [1]_.



### Organization of the document


- Overall workflow in dual-core communication provides an overall workflow of
  dual-core communication between NSPE and SPE.
- Mailbox communication Requirements lists general requirements of
  mailbox, from the perspective of dual-core communication.
- PSA client call handling flow in TF-M discusses about the detailed sequence
  and key modules of handling PSA client call in TF-M.
