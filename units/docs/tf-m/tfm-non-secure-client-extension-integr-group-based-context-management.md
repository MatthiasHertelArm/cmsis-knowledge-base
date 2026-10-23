---
id: "tfm-non-secure-client-extension-integr-group-based-context-management"
type: "concept"
domain: "security"
title: "Non-secure Client Extension Integration Guide: Group-based context management"
summary: "NSCE introduces a group-based context management for NS clients. The purpose is to support diverse use scenarios in the IoT world."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/non-secure_client_extension_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/non-secure_client_extension_integration_guide.html#group-based-context-management"
license: "BSD-3-Clause"
mode: "V"
---

NSCE introduces a group-based context management for NS clients. The purpose is
to support diverse use scenarios in the IoT world.

For rich-resource devices, TF-M could assign separate contexts for each
connection. For resource-constrained devices, TF-M may support very limited
context slots. Multiple NS connections could share the same context provided
they have mutual exclusion access to the secure services.

To support this flexibility, a group ID (gid) and a thread ID (tid) are
specified for the connection of the NS client. NSCE allocates only one context
for a given group. Threads in the same group share the context.

The gid and tid are specified by NSPE RTOS via NSCE interface.
