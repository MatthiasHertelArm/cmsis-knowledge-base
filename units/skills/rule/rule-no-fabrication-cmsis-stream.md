---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-cmsis-stream"
constrains: ["proc-cmsis-stream"]
---

Do not assume component properties or invent CMSIS Stream APIs, event names, parameter definitions, state-management behavior, paths, or validation results. Ask the user for all missing information needed to generate a complete and accurate component description.
