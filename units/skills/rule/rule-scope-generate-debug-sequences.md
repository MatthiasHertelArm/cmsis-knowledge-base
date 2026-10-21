---
type: "rule"
title: "Scope"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-scope-generate-debug-sequences"
constrains: ["proc-generate-debug-sequences"]
---

Generate only non-trace sequences and related documented runtime choices. Preserve trace configuration and unrelated PDSC content; do not modify `.dbgconf` without explicit confirmation.
