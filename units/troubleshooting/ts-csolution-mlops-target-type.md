---
id: "ts-csolution-mlops-target-type"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops: target type"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["mlops: target type '<…>' not found"]
symptom_regex: "^mlops: target type '.+?' not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrMlops.cpp:78"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`mlops: target type '<…>' not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!FindTargetType(csolution, target.targetType, targetType)) {
```
