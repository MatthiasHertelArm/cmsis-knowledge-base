---
type: "rule"
title: "Do not invent trace component addresses, identifiers, versions,"
severity: "must"
status: "draft"
shared: false
id: "rule-unnamed-trace-knowledge"
constrains: ["proc-trace-knowledge"]
---

Do not invent trace component addresses, identifiers, versions, DP/AP paths, routes, trace-clock control, pin-function or electrical configuration, path-selection controls, sink behavior, or device-specific lifecycle constraints. Return missing reusable access facts to `$debug-access-knowledge`.
