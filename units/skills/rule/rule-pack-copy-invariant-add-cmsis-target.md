---
type: "rule"
title: "Pack copy invariant"
severity: "must"
status: "draft"
shared: false
id: "rule-pack-copy-invariant-add-cmsis-target"
constrains: ["proc-add-cmsis-target"]
---

Copy the selected layer into the project and reference the local copy; never bind the project to a layer inside the installed pack.
