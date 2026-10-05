---
id: "tfm-secure-partition-manager-runtime-management"
type: "concept"
domain: "security"
title: "Secure Partition Manager: Runtime management"
summary: "The runtime execution runs among the components, there are 4 runtime states:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/secure_partition_manager.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_manager.html#runtime-management"
license: "BSD-3-Clause"
mode: "V"
---

The runtime execution runs among the components, there are **4** runtime
states:

- `Initializing` state, to set up the SPM runtime environment after system
  powers up
- `IDLE` state, when SPM runtime environment is set up and partitions are
  ready for service access.
- `Serving` state, when partition is under initializing or service access
  handling.
- `Background` state, such as the arrival of secure interrupt or unexpected
  faults. `Background` state returns to the state it preempts. `Background`
  state can be nested.

The state transition diagram:
