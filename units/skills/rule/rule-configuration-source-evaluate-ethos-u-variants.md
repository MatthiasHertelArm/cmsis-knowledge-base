---
type: "rule"
title: "Configuration source"
severity: "must"
status: "draft"
shared: false
id: "rule-configuration-source-evaluate-ethos-u-variants"
constrains: ["proc-evaluate-ethos-u-variants"]
---

Use `Arm/vela.ini` from the active Vela installation by default. Do not silently substitute a workspace or device-specific file. Use a device-specific file only when the user provides it.
