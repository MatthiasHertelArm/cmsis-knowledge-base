---
id: "tfm-secure-partition-manager-background-state"
type: "concept"
domain: "security"
title: "Secure Partition Manager: Runtime management / Background state"
summary: "Background execution can happen at any time when the arrival of interrupts or execution faults. An ongoing background execution indicates the state is a Background state. The characteristics:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/secure_partition_manager.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/secure_partition_manager.html#background-state"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Runtime management_

Background execution can happen at any time when the arrival of interrupts or
execution faults. An ongoing background execution indicates the state is a
`Background state`. The characteristics:

- The background state has a higher execution priority than other states -
  other states stall when the background state is executing.
- Background execution can be nested. For example, an
  interrupt handler can preempt an ongoing interrupt execution.
- Particular partition code can be involved in the background state, for
  example, the `First Level Interrupt Handler (FLIH)` of one partition.
- Background state MUST return to the state it preempts.


**Note:** Interrupt handling is a common background state example. Check Interrupt design document for details.
