---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-no-fabrication-cmsis-stream"
constrains: ["proc-cmsis-stream"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Do not assume component properties or invent CMSIS Stream APIs, event names, parameter definitions, state-management behavior, paths, or validation results. Ask the user for all missing information needed to generate a complete and accurate component description.

## Delta zu rule-no-fabrication

assume component properties or invent CMSIS Stream APIs, event names, parameter definitions, state-management behavior, paths, or validation results. Ask the user for all missing information needed to generate a complete and accurate component description.
