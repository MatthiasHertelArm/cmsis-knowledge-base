---
type: "rule"
title: "Scope"
severity: "must"
status: "draft"
shared: false
id: "rule-scope-check-pyocd-availability"
constrains: ["proc-check-pyocd-availability"]
---

Check availability only. Use `$pyocd-detect-debug-topology` for an authorized target scan after pyOCD availability is established.
