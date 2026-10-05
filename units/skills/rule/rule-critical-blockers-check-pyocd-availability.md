---
type: "rule"
title: "Critical blockers"
severity: "must"
status: "draft"
shared: false
id: "rule-critical-blockers-check-pyocd-availability"
constrains: ["proc-check-pyocd-availability"]
---

Report the relevant check as unavailable when the required terminal, extension query, or extension directory cannot be accessed. Do not search unrelated directories or request a target connection.
