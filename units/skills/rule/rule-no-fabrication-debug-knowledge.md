---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-debug-knowledge"
constrains: ["proc-debug-knowledge"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Do not invent reset, unlock, authentication, boot, flash, processor-control, low-power behavior, or board routing. Return missing connection, protocol, DP/AP, or dormant-state facts to `$debug-access-knowledge`.

## Delta zu rule-no-fabrication

reset, unlock, authentication, boot, flash, processor-control, low-power behavior, or board routing. Return missing connection, protocol, DP/AP, or dormant-state facts to `$debug-access-knowledge`.
