---
id: "ts-csolution-it-must-be-latest-all-or-required"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: , it must be 'latest', 'all' or 'required"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["unknown load option: '<…>', it must be 'latest', 'all' or 'required'"]
symptom_regex: "^unknown load option: '.+?', it must be 'latest', 'all' or 'required'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:478"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`unknown load option: '<…>', it must be 'latest', 'all' or 'required'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
} else if (m_loadPacksPolicy == "required") {
```
