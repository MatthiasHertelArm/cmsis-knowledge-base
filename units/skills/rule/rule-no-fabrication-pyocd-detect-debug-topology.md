---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-no-fabrication-pyocd-detect-debug-topology"
constrains: ["proc-pyocd-detect-debug-topology"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Do not infer device behavior, reset behavior, unlock requirements, dormant-state requirements, a missing component, or an undocumented address from a scan or its absence.

## Delta zu rule-no-fabrication

device behavior, reset behavior, unlock requirements, dormant-state requirements, a missing component, or an undocumented address from a scan or its absence
