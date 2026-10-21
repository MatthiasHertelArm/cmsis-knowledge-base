---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-critical-blockers-evaluate-ethos-u-variants"
constrains: ["proc-evaluate-ethos-u-variants"]
---

Return `FAIL` and stop when the model is missing, unreadable, represented only by a Git LFS pointer, or has another extension; when `vela` is unavailable or cannot report its version; when the selected configuration cannot be read; when the shared deadline expires; when a Vela compile fails; or when a summary CSV is absent or incomplete.
