---
id: "tfm-communication-between-nspe-and-spe-psa-client-call-handling-flow-in-tf-m"
type: "concept"
domain: "security"
title: "Communication Between NSPE And SPE In Dual Core System: PSA client call handling flow in TF-M"
summary: "This section describes how TF-M processes PSA client call requests:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/communication_between_nspe_and_spe_in_dual_core_systems.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/communication_between_nspe_and_spe_in_dual_core_systems.html#psa-client-call-handling-flow-in-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

This section describes how TF-M processes PSA client call requests:

1. Platform specific Inter-Processor Communication interrupt handler is
   triggered after the mailbox event is asserted by NSPE. The interrupt handler
   calls `spm_handle_interrupt()`.
2. SPM sends a `MAILBOX_INTERRUPT_SIGNAL` to `ns_agent_mailbox` partition.
3. `ns_agent_mailbox` partition deals with the mailbox message(s) which
   contain(s) the PSA client call information and parameters.
   Then the PSA client call request is dispatched to dedicated PSA client call
   handler in TF-M SPM.
4. After the PSA client call completes, the return value is transmitted to NSPE
   via mailbox.

Key modules and components:

- Inter-Processor Communication interrupt handler discusses the
  Inter-Processor Communication interrupt handler
- TF-M Remote Procedure Call (RPC) layer introduces TF-M Remote Procedure
  Call layer to support dual-core communication.
- ns_agent_mailbox partition describes the mailbox agent partition.
- Return value response routine in TF-M proposes the routine to send the
  return value to NSPE.



### Inter-Processor Communication interrupt handler


Platform specific driver must implement the Inter-Processor Communication
interrupt handler to deal with the Inter-Processor Communication interrupt
asserted by NSPE.
The platform specific interrupt handler shall complete the interrupt
operations, such as interrupt EOI or acknowledge.

The interrupt handler calls `spm_handle_interrupt()` to notify SPM of the
interrupt.

The platform's `tfm_peripherals_def.h` file defines a macro `MAILBOX_IRQ`
that identifies the interrupt being used. The platform must also provide a
function `mailbox_irq_init()` that initialises the interrupt as described
in [2]_.

Platform specific driver puts Inter-Processor Communication interrupt into a
proper exception priority, according to system and application requirements.
The priority setting must guarantee that:

- TF-M may respond to a PSA client call request in time according to system and
  application requirements.
- Other exceptions, which are more latency sensitive or require higher
  priorities, are not blocked by Inter-Processor Communication interrupt ISR.

The exception priority setting is IMPLEMENTATION DEFINED.



### TF-M Remote Procedure Call (RPC) layer


The RPC layer sits between TF-M SPM and mailbox implementation. The purpose of
RPC layer is to decouple mailbox implementation and TF-M SPM and enhance the
generality of entire dual-core communication.

The RPC layer provides a set of APIs to TF-M SPM to handle and reply PSA client
call from NSPE in dual-core scenario.
It hides the details of specific mailbox implementation from TF-M SPM. It avoids
modifying TF-M SPM to fit mailbox development and changes.
It can keep a unified PSA client call process in TF-M SPM in both single
Armv8-M scenario and dual-core scenario.

The RPC layer defines a set callback functions for mailbox implementation to
hook its specific mailbox operations. When TF-M SPM invokes RPC APIs to deal
with NSPE PSA client call, RPC layer eventually calls the callbacks to execute
mailbox operations.
RPC layer also defines a set of PSA client call handler APIs for mailbox
implementation. RPC specific client call handlers parse the PSA client call
parameters and invoke common TF-M PSA client call handlers.



### ns_agent_mailbox partition


A dedicated agent acts as a partition and interacts with the NSPE through the
mailbox.

First, the agent calls `tfm_hal_boot_ns_cpu()` and
`tfm_hal_wait_for_ns_cpu_ready()` to prepare the non-secure core.
Then it initialises the SPE mailbox and enable the IPC interrupt.

Once these tasks are complete, it enters an infinite loop waiting for a
`MAILBOX_INTERRUPT_SIGNAL` signal indicating that a mailbox message has
arrived.

Mailbox handling is performed in the context of the `ns_agent_mailbox`
partition, which makes any necessary calls to other partitions on behalf of
the non-secure code.

`ns_agent_mailbox` calls RPC API `tfm_rpc_client_call_handler()` to check
and handle PSA client call requests from NSPE.

`tfm_rpc_client_call_handler()` invokes request handling callback function to
execute specific mailbox message handling operations.
More details in document [1]_.

The handling process in mailbox operation consists of the following steps:

1. SPE mailbox fetches the PSA client call parameters from NSPE mailbox.
   Proper protection and synchronization must be implemented in mailbox to
   guarantee that the operations are not interfered with by NSPE mailbox
   operations or Inter-Processor Communication interrupt handler.
   If a queue is maintained inside TF-M core, SPE mailbox can fetch multiple
   PSA client calls together into the queue, to save the time of synchronization
   between two cores.

2. SPE mailbox parses the PSA client call parameters copied from NSPE, including
   the PSA client call type.

3. The PSA client call request is dispatched to the dedicated TF-M RPC PSA
   client call handler. The PSA client call request is processed in the
   corresponding handler based on PSA call types.

The dual-core scenario and single Armv8-M scenario in TF-M IPC implementation
shares the same PSA client call routines inside TF-M SPM. The current
handler definitions can be adjusted to be more generic for dual-core scenario
and single Armv8-M implementation.

If multiple requests are pending, the mailbox processes them one by one.



### Return value response routine in TF-M


Diverse PSA client calls can be implemented with different return value replying
routines.



#### Replying routine for psa_framework_version() and psa_version()


For `psa_framework_version()` and `psa_version()`, handlers return values
directly during mailbox processing.
A compile flag can enable this routine for dual-core builds.

For `psa_connect()`, `psa_call()`, and `psa_close()`, the target secure
partition completes the client call and invokes `psa_reply()`.
The SVC handler in TF-M SPM then calls `tfm_rpc_client_call_reply()` to return
the result via mailbox.

Mailbox reply functions must not trigger context switches inside the SVC
handler.

If errors occur, the RPC handlers return the error without invoking the secure
partition. The mailbox transmits the error code to NSPE.



### Build options


The feature is enabled by `TFM_MULTI_CORE_TOPOLOGY`.
