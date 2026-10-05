---
type: "rule"
title: "Schema integrity"
severity: "must"
status: "draft"
shared: false
id: "rule-schema-integrity-add-cmsis-target"
constrains: ["proc-add-cmsis-target"]
---

Use `csolution convert` with its default schema checking. Do not pass `--no-check-schema`, run a redundant schema-validation step, or alter a schema to make invalid project YAML pass.
