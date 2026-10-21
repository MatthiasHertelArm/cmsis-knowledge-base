---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-critical-blockers-start-zephyr-project"
constrains: ["proc-start-zephyr-project"]
---

Stop before writing project files when a prerequisite fails, required values are absent or ambiguous, a compiler choice is unresolved, or either required validation command fails.
