---
type: "rule"
title: "Fail fast"
severity: "must"
status: "draft"
shared: false
id: "rule-fail-fast-evaluate-ethos-u-variants"
constrains: ["proc-evaluate-ethos-u-variants"]
---

Do not continue with remaining candidates or optimization settings after a fatal error. Preserve the failed build's `vela.log` when an output directory has already been created.
