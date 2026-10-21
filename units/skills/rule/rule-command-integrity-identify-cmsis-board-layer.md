---
type: "rule"
title: "Command integrity"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-command-integrity-identify-cmsis-board-layer"
constrains: ["proc-identify-cmsis-board-layer"]
---

Require `csolution list layers` to support and use `--verbose`. Stop on any `csolution` command-line syntax or option-parsing error; do not retry with modified options.
