---
type: "rule"
title: "Output safety"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-output-safety-evaluate-ethos-u-variants"
constrains: ["proc-evaluate-ethos-u-variants"]
---

Use a separate build directory for every candidate and optimization setting. Do not overwrite a non-empty user-selected output directory.
