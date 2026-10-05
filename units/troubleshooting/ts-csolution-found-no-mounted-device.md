---
id: "ts-csolution-found-no-mounted-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: found no mounted device"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["found no mounted device"]
symptom_regex: "^found no mounted device$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1440"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`found no mounted device`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
} else if (mountedDevices.size() == 0) {
```
