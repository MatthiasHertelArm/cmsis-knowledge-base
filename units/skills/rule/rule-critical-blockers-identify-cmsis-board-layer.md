---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-critical-blockers-identify-cmsis-board-layer"
constrains: ["proc-identify-cmsis-board-layer"]
---

Stop on a missing target, mismatch with the verified identity, unavailable required pack, unsupported required `csolution` option, `csolution` syntax or option-parsing error, failed layer query, missing candidate source, or ambiguous active context that cannot be resolved from the project.
