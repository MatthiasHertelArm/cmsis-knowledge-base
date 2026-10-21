---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-portability-identify-cmsis-board-layer"
constrains: ["proc-identify-cmsis-board-layer"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Do not add a device-family, toolchain, debugger, build-system, or RTOS assumption beyond the verified target, input project, or candidate metadata.

## Delta zu rule-portability

build-system, or RTOS assumption beyond the verified target, input project, or candidate metadata.
