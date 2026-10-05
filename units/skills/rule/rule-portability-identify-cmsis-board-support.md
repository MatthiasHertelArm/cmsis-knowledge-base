---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
shared: false
id: "rule-portability-identify-cmsis-board-support"
constrains: ["proc-identify-cmsis-board-support"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Do not add vendor, toolchain, RTOS, debugger, or probe assumptions beyond the verified catalog result.

## Delta zu rule-portability

RTOS, debugger, or probe assumptions beyond the verified catalog result.
