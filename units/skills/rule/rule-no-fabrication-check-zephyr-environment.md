---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-check-zephyr-environment"
constrains: ["proc-check-zephyr-environment"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Do not invent workspace paths, executable paths, Zephyr repository locations, or command results.

## Delta zu rule-no-fabrication

workspace paths, executable paths, Zephyr repository locations, or command results
