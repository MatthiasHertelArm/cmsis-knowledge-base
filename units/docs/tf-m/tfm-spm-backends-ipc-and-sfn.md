---
id: "tfm-spm-backends-ipc-and-sfn"
type: "concept"
domain: "security"
title: "SPM Backends: IPC and SFN"
summary: "The Firmware Framework M (FF-M) [1], [2] provides two different programming models for Secure Partitions."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/spm_backends.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/spm_backends.html#ipc-and-sfn"
license: "BSD-3-Clause"
mode: "V"
---

The Firmware Framework M (FF-M) [1]_, [2]_ provides two different programming
models for Secure Partitions.

- IPC Model

  The Secure Partition processes signals in any order, and can defer
  responding to a message while continuing to process other signals.

- SFN Model

  The Secure Partition is made up of a collection of callback functions which
  implement secure services.

Although the programming model is different, they share the same APIs to
interact with the SPM.
The behaviours of the APIs share the same implementation with slight differences
for the two programming models.
This is regarded as the `frontend`.

The TF-M runtime implementations behind `frontend` are different.
TF-M provides two `backends` correspondingly.

 - IPC backend

  In this backend, the SPM and each Secure Partition have their own execution
  contexts, which is required to support the IPC model Secure Partitions.
  This also enables the SPM to provide higher isolation levels.
  This SPM backend acts like a multiple-process system.
  It can also adopt SFN model Secure Partitions.

 - SFN backend

  The SFN backend provides more efficient executions because it shares a
  single-thread execution context with all the Secure Partitions.
  This SPM backend acts like a single library.
  Therefore, it can only adopt SFN model Secure Partitions.
  And it does not support higher isolation levels.
  On the other hand, it consumes less memory compared to the IPC backend.

The following table summaries the relationships between SPM backends, Secure
Partition models and isolation levels.


+--------------+---------------------------+---------------------------+
| SPM backend  | Supported Partition model | Supported Isolation Level |
+==============+===========================+===========================+
| SFN          | SFN Partition             | 1                         |
+--------------+---------------------------+---------------------------+
| IPC          | IPC and SFN Partition     | 1, 2 and 3                |
+--------------+---------------------------+---------------------------+
