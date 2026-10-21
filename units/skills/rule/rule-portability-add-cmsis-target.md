---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-portability-add-cmsis-target"
constrains: ["proc-add-cmsis-target"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Do not introduce a device-family, toolchain, debugger, build-system, or RTOS dependency unless the verified target, selected layer, or existing project requires it. Identify every such dependency in the output.

## Delta zu rule-portability

build-system, or RTOS dependency unless the verified target, selected layer, or existing project requires it. Identify every such dependency in the output.
