---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
shared: false
id: "rule-no-fabrication-generate-debug-description"
constrains: ["proc-generate-debug-description"]
---

Do not invent topology facts, addresses, protocols, patches, values, or applicability. Return missing or contradictory hardware facts to `$debug-access-knowledge`.
