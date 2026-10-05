---
id: "tfm-communication-between-nspe-and-spe-mailbox-communication-requirements"
type: "concept"
domain: "security"
title: "Communication Between NSPE And SPE In Dual Core System: Mailbox communication Requirements"
summary: "The communication between NSPE and SPE relies on mailbox communication implementation. The mailbox functionalities are eventually implemented by platform specific Inter-Processor Communication drivers. This section lists some general requirements on mailbox communication between NSPE and SPE."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/multi-cpu/communication_between_nspe_and_spe_in_dual_core_systems.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/communication_between_nspe_and_spe_in_dual_core_systems.html#mailbox-communication-requirements"
license: "BSD-3-Clause"
mode: "V"
---

The communication between NSPE and SPE relies on mailbox communication
implementation. The mailbox functionalities are eventually implemented by
platform specific Inter-Processor Communication drivers.
This section lists some general requirements on mailbox communication between
NSPE and SPE.



### Data exchanged between NPSE and SPE


A mailbox message contains the information and parameters of a PSA client call.
After SPE is notified by a mailbox event, SPE fetches the parameters from NSPE
for PSA Client call processing.
The mailbox design document [1]_ defines the structure of the mailbox message.

The information and parameters of PSA Client call in the mailbox message include

- PSA Client API

- Parameters required in PSA Client call. The parameters can include the
  following, according to PSA client call type:

  - Service ID (SID)
  - Handle
  - Request type
  - Input vectors and the lengths
  - Output vectors and the lengths
  - Requested version of secure service

- NSPE Client ID. Optional. The NSPE Client ID is required when NSPE RTOS
  enforces non-secure task isolation.

The mailbox implementation may define additional members in mailbox message to
accomplish mailbox communication between NSPE and SPE.

When the PSA Client call is completed in TF-M, the return result, such as
PSA_SUCCESS or a handle, shall be returned from SPE to NSPE via mailbox.



### Synchronization between NSPE and SPE


The system must protect shared mailbox objects and variables from concurrent
access by NSPE and SPE.

Synchronization mechanisms must prevent race conditions when both cores access
the mailbox.



### Support of multiple concurrent calls (informative)


If the support of multiple ongoing NS PSA client calls in TF-M is required
in dual-core systems, an optional queue can be maintained in TF-M core to store
multiple mailbox objects received from NSPE.
To identify NS PSA client calls, additional fields can be added in TF-M SPM
objects to store the NS PSA Client request identification.

Note that when just a single outstanding PSA client call is allowed, multiple
NSPE OS threads can run concurrently and call PSA client functions. The first
PSA client call will be processed first, and any other OS threads will be
blocked from submitting PSA client calls until the first is completed.
