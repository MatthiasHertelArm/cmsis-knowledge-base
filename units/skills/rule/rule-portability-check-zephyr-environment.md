---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
shared: false
id: "rule-portability-check-zephyr-environment"
constrains: ["proc-check-zephyr-environment"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Use only the documented platform-specific venv paths; do not introduce board, MCU, toolchain, or debugger assumptions.

## Delta zu rule-portability

Use only the documented platform-specific venv paths
