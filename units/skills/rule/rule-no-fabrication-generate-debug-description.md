---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-generate-debug-description"
constrains: ["proc-generate-debug-description"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Do not invent topology facts, addresses, protocols, patches, values, or applicability. Return missing or contradictory hardware facts to `$debug-access-knowledge`.

## Delta zu rule-no-fabrication

topology facts, addresses, protocols, patches, values, or applicability. Return missing or contradictory hardware facts to `$debug-access-knowledge`.
