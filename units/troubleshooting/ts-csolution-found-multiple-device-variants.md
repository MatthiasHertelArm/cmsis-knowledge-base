---
id: "ts-csolution-found-multiple-device-variants"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: found multiple device variants"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["found multiple device variants"]
symptom_regex: "^found multiple device variants$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1504"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`found multiple device variants`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (matchedDevice->GetDeviceItemCount() > 0) {
```
