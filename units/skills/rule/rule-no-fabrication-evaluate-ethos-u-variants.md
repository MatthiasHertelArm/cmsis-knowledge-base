---
type: "rule"
title: "No fabrication"
severity: "must"
status: "draft"
license: "Apache-2.0"
shared: false
id: "rule-no-fabrication-evaluate-ethos-u-variants"
constrains: ["proc-evaluate-ethos-u-variants"]
refines: ["rule-no-fabrication"]
delta_of: "rule-no-fabrication"
---

Report only values read from Vela's generated summary CSV and console output. Do not infer successful NPU placement or missing measurements.

## Delta zu rule-no-fabrication

Report only values read from Vela's generated summary CSV and console output. Do not infer successful NPU placement or missing measurements.
