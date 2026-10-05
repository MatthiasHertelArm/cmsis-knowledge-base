---
id: "ts-csolution-processor-name"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processor name"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processor name '<…>' was not found"]
symptom_regex: "^processor name '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1517"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`processor name '<…>' was not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!deviceItem.pname.empty()) {
```
