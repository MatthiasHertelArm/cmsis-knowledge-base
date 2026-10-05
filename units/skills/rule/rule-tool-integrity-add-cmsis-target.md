---
type: "rule"
title: "Tool integrity"
severity: "must"
status: "draft"
shared: false
id: "rule-tool-integrity-add-cmsis-target"
constrains: ["proc-add-cmsis-target"]
---

Do not edit the project unless `check-cmsis-environment` passes and the required `cbuild`, `csolution`, and `cpackget` commands resolve from the same compatible CMSIS-Toolbox installation.
