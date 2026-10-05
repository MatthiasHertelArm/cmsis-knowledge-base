---
id: "ts-csolution-export-file-cannot-be-written"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: export file cannot be written"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["export file cannot be written"]
symptom_regex: "^export file cannot be written$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:811"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`export file cannot be written`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (m_generator.GenerateCprj(*contextItem, exportfilename, true)) {
```
