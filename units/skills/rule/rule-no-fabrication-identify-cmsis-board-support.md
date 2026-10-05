---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-identify-cmsis-board-support"
constrains: ["proc-identify-cmsis-board-support"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Do not invent CMSIS board, device, BSP, or DFP identifiers, and do not infer support from a similar part name.

## Delta zu rule-no-fabrication

CMSIS board, device, BSP, or DFP identifiers, and do not infer support from a similar part name.
