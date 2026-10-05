---
type: "rule"
title: "Preserve READY unless an affected fact becomes stale,"
severity: "must"
status: "draft"
shared: false
id: "rule-unnamed-trace-knowledge-4"
constrains: ["proc-trace-knowledge"]
---

Preserve `READY` unless an affected fact becomes stale, contradictory, or insufficient. Use `BLOCKED` only when a required input is unavailable and name that input.
