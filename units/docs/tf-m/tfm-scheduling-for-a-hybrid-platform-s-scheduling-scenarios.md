---
id: "tfm-scheduling-for-a-hybrid-platform-s-scheduling-scenarios"
type: "concept"
domain: "security"
title: "Scheduling for a Hybrid Platform Solution: Scheduling Scenarios"
summary: "There are commonly two classes of scheduling use-cases depending on how the workload importance is distributed:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/hybrid_platform_solution.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/hybrid_platform_solution.html#scheduling-scenarios"
license: "BSD-3-Clause"
mode: "V"
---

There are commonly two classes of scheduling use-cases depending on how the
workload importance is distributed:

- Local NSPE can be interrupted anytime when a secure service is requested by
  the remote clients.
- Local NSPE can NOT be interrupted when a secure service is requested by the
  remote clients.

Usually, it is known at design stage which types of workloads and applications
will run in both local and remote clients, thus it can be decided in advance
which class of clients require to be serviced immediately and/or can be
preempted.
Such knowledge is then used to decide which scheduling option is best for the
whole system.

Those options are generalized and provided with three build choices assigned to
the build config `CONFIG_TFM_HYBRID_PLAT_SCHED_TYPE`.


+-----------------------------------+----------------------------------------------------------+
| CONFIG_TFM_HYBRID_PLAT_SCHED_TYPE | Description                                              |
+===================================+==========================================================+
| TFM_HYBRID_PLAT_SCHED_OFF         | No support for Hybrid Platform is provided.              |
| (Default)                         |                                                          |
+-----------------------------------+----------------------------------------------------------+
| TFM_HYBRID_PLAT_SCHED_SPE         | NSPE has no control over when the request is processed.  |
|                                   |                                                          |
|                                   | SPE preempts NSPE (is scheduled to run) and runs the     |
|                                   | requested secure service (by the remote client).         |
|                                   | Once completed, execution then resumes to NSPE.          |
|                                   |                                                          |
+-----------------------------------+----------------------------------------------------------+
| TFM_HYBRID_PLAT_SCHED_NSPE        | NSPE is in full control over the incoming requests from  |
|                                   | the remote clients.                                      |
|                                   |                                                          |
|                                   | The incoming requests may be queued but execution does   |
|                                   | not switch to SPE.                                       |
|                                   | The local NSPE makes its own decisions on when it is     |
|                                   | an appropriate point to yield execution to execute the   |
|                                   | mailbox requests.                                        |
|                                   |                                                          |
|                                   | To do so, NSPE performs a psa_call to a stateless service|
|                                   | in the mailbox partition and let the execution to proceed|
|                                   | in SPE.                                                  |
|                                   | Note that the local NSPE does not have knowledge of any  |
|                                   | pending messages in the mailbox awaiting processing.     |
|                                   | It can only attempt to start their processing.           |
|                                   |                                                          |
+-----------------------------------+----------------------------------------------------------+
| TFM_HYBRID_PLAT_SCHED_BALANCED    | When multiple mailbox channels, and their respective     |
|                                   | interrupts, are available on a platform, then it is      |
|                                   | possible to schedule independently the different sources.|
|                                   | That is, some messages can be configured to be scheduled |
|                                   | according to the `SCHED_SPE` mechanism, while others   |
|                                   | can be configured to be scheduled according to the       |
|                                   | `SCHED_NSPE` (deferred to local NSPE) mechanism.       |
|                                   |                                                          |
|                                   | This can be achieved via a special attribute in the      |
|                                   | manifest: `mbox_flags`.                                |
+-----------------------------------+----------------------------------------------------------+

The definitions for the options above are available in
`secure_fw/spm/include/tfm_hybrid_platform.h`.
