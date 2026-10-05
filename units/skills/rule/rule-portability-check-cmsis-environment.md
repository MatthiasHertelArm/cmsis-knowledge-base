---
type: "rule"
title: "Portability"
severity: "must"
status: "draft"
shared: false
id: "rule-portability-check-cmsis-environment"
constrains: ["proc-check-cmsis-environment"]
refines: ["rule-portability"]
delta_of: "rule-portability"
---

Do not add persistent host settings or assume a compiler family beyond the artifacts selected by the workspace.

## Delta zu rule-portability

Do not add persistent host settings … beyond the artifacts selected by the workspace.
