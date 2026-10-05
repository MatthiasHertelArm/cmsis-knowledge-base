---
id: "x-cmsis-pack-docs-2"
type: "concept"
domain: "bring-up"
title: "Which Arm document defines which debug fact"
status: "draft"
extracted_from: "proc-cmsis-pack-docs"
source: "cmsis-pack-docs/SKILL.md"
---

Arm documents only for the facts that are Arm's to define — DP/AP behaviour, dormant state and `TARGETSEL` (`ihi0031`), APv2 addressing and ROM tables (`ihi0074`), DHCSR/DEMCR/AIRCR reset and halt semantics and debug authentication (`ddi0419`/`ddi0403`/`ddi0553`), fixed PPB addresses, TPIU port sizes and SWO modes (core TRM), identifying a scanned CoreSight component by its part number (CoreSight TRMs). Do **not** fetch CoreSight TRMs to program funnels, replicators, ETF/ETB/ ETR, TPIU or SWO: the trace generator templates own that.
