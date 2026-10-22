---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-critical-blockers-pyocd-detect-debug-topology"
constrains: ["proc-pyocd-detect-debug-topology"]
---

Stop when a new scan lacks a successful `$check-pyocd-availability` result, an accessible target, a selection among multiple attached targets, or documented unlock/power-up steps for a repeat scan.
