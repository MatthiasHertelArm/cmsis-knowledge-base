---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-no-fabrication-generate-debug-sequences"
constrains: ["proc-generate-debug-sequences"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Do not invent reset, unlock, authentication, boot, flash, processor-control, low-power, register, delay, or connection behavior.

## Delta zu rule-no-fabrication

reset, unlock, authentication, boot, flash, processor-control, low-power, register, delay, or connection behavior
