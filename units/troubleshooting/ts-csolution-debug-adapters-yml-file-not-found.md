---
id: "ts-csolution-debug-adapters-yml-file-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: debug-adapters.yml file not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["debug-adapters.yml file not found"]
symptom_regex: "^debug\\-adapters\\.yml file not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:939"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`debug-adapters.yml file not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (debugAdapters.empty()) {
```
