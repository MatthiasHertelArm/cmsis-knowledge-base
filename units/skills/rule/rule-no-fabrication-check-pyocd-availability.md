---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-no-fabrication-check-pyocd-availability"
constrains: ["proc-check-pyocd-availability"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Do not infer an executable path, extension location, version, or availability from the extension identifier alone.

## Delta zu rule-no-fabrication

executable path, extension location, version, or availability from the extension identifier alone
