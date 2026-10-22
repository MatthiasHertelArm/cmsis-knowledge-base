---
id: "tfm-adding-secure-partition-introduction"
type: "concept"
domain: "security"
title: "Adding Secure Partition: Introduction"
summary: "Secure Partition is an execution environment that provides the following functions to Root of Trust (RoT) Services:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_secure_partition_addition.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_secure_partition_addition.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

Secure Partition is an execution environment that provides the following
functions to Root of Trust (RoT) Services:

- Access to resources, protection of its own code and data.
- Mechanisms to interact with other components in the system.

Each Secure Partition is a single thread of execution and the smallest unit of
isolation.

This document mainly describes how to add a secure partition in TF-M and
focuses on the configuration, manifest, implement rules. The actual
source-level implementation is not included in this document.

If not otherwise specified, the steps are identical for IPC and SFN model.

The IPC and SFN model conforms to the *PSA Firmware Framework for M (FF-M) v
1.1* changes. Refer to PSA Firmware Framework specification and
Firmware Framework for M 1.1 Extensions for details.
