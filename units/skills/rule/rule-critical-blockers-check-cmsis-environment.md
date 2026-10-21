---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-critical-blockers-check-cmsis-environment"
constrains: ["proc-check-cmsis-environment"]
---

Stop when a selected artifact is absent or ambiguous, `cbuild` is unavailable, or a required environment check fails.
