---
id: "ts-csolution-is-listed-multiple-times"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is listed multiple times"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["conflict: component '<…>' is listed multiple times"]
symptom_regex: "^conflict: component '.+?' is listed multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3909"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`conflict: component '<…>' is listed multiple times`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (ignoreDuplicates) {
```
