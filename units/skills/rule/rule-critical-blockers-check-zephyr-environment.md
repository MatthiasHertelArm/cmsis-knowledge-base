---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-check-zephyr-environment"
constrains: ["proc-check-zephyr-environment"]
---

Stop at the first missing workspace, virtual environment, executable, failed command, or mismatched west top-level directory.
