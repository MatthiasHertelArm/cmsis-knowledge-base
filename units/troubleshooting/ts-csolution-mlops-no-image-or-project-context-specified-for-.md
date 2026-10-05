---
id: "ts-csolution-mlops-no-image-or-project-context-specified-for-"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops: no image or project-context specified for target"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["mlops: no image or project-context specified for target '<…>'"]
symptom_regex: "^mlops: no image or project\\-context specified for target '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrMlops.cpp:201"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`mlops: no image or project-context specified for target '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!t.targetType.empty() && ref.empty()) {
```
