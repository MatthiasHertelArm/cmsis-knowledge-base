---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-portability-pyocd-detect-debug-topology"
constrains: ["proc-pyocd-detect-debug-topology"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Do not introduce a target, probe, device-family, toolchain, or operating-system assumption beyond the active scan context.

## Delta zu rule-portability

operating-system assumption beyond the active scan context
