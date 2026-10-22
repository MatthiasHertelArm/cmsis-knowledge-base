---
id: "tfm-secure-partition-manager-idle-state"
type: "concept"
domain: "security"
title: "Secure Partition Manager: Runtime management / IDLE state"
summary: "The IDLE state can be represented by the NS Agent action:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/secure_partition_manager.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_manager.html#idle-state"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Runtime management_

The `IDLE state` can be represented by the `NS Agent` action:

- Launching NSPE software (Trustzone case, e.g.), or send a signal to NSPE
  software (RPC case, e.g.).

It is because `NS Agent` is the last component being initialized in the
system. Its execution indicates other partitions' initialization has
accomplished.
