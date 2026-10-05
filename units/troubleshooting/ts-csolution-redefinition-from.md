---
id: "ts-csolution-redefinition-from"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: redefinition from"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["redefinition from '<…>' into '<…>' is not allowed"]
symptom_regex: "^redefinition from '.+?' into '.+?' is not allowed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:797"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`redefinition from '<…>' into '<…>' is not allowed`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!outValue.empty() && (outValue != element)) {
```
