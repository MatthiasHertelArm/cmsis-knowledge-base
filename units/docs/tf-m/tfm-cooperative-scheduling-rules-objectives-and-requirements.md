---
id: "tfm-cooperative-scheduling-rules-objectives-and-requirements"
type: "concept"
domain: "security"
title: "Cooperative Scheduling Rules: Objectives and Requirements"
summary: "a. NSPE interrupt handling implementation should be independent b. Impact on the NSPE scheduler should be minimal c. No assumptions should be made about NSPE's scheduling capabilities"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/tfm_cooperative_scheduling_rules.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/tfm_cooperative_scheduling_rules.html#objectives-and-requirements"
license: "BSD-3-Clause"
mode: "V"
---

1. Decoupling of scheduling decisions between NSPE and SPE
2. Efficient interrupt handling by SPE as well as NSPE
3. Reduce critical sections on the secure side to not block interrupts
   unnecessarily
4. Scalability to allow simplification/reduction of overheads to scale down the
   design for constrained devices
5. Reduce impact on NSPE software design

  a. NSPE interrupt handling implementation should be independent
  b. Impact on the NSPE scheduler should be minimal
  c. No assumptions should be made about NSPE's scheduling capabilities
