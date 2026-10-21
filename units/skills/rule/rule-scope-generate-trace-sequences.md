---
type: "rule"
title: "Scope"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-scope-generate-trace-sequences"
constrains: ["proc-generate-trace-sequences"]
---

Generate only full-mode CoreSight trace configuration. Preserve unrelated PDSC content; do not create legacy setup, omit verified paths, or modify `.dbgconf` without explicit confirmation.
