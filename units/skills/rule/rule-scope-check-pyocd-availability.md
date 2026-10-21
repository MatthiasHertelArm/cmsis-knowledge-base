---
type: "rule"
title: "Scope"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-scope-check-pyocd-availability"
constrains: ["proc-check-pyocd-availability"]
---

Check availability only. Use `proc-pyocd-detect-debug-topology` (`knowledge_get`) for an authorized target scan after pyOCD availability is established.
