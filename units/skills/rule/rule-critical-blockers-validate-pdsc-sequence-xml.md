---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-validate-pdsc-sequence-xml"
constrains: ["proc-validate-pdsc-sequence-xml"]
---

Stop when `packchk` or required XML/PDSC validation cannot run, a required match remains unresolved, or the target PDSC is unavailable.
