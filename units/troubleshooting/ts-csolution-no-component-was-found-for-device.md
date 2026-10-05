---
id: "ts-csolution-no-component-was-found-for-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no component was found for device"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no component was found for device '<…>'"]
symptom_regex: "^no component was found for device '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:4463"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no component was found for device '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!selectedContext.empty()) {
```
