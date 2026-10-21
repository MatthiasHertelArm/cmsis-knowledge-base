---
id: "x-add-board-layer-3"
type: "concept"
domain: "project"
title: "Register read-back tells: wrong address or unclocked peripheral"
status: "draft"
extracted_from: "proc-add-board-layer"
source: "add-board-layer/SKILL.md"
license: "Apache-2.0"
---

Tells: reads-back-0 always → reserved/wrong address; several registers of one peripheral reading the **same** value → the peripheral is unclocked and the bus is echoing garbage. When the hardware disagrees with the manual, search the errata document before changing code.
