---
id: "ts-csolution-was-not-found-in-global-register"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: was not found in global register"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator '<…>' required by component '<…>' was not found in global register"]
symptom_regex: "^generator '.+?' required by component '.+?' was not found in global register$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrExtGenerator.cpp:35"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`generator '<…>' required by component '<…>' was not found in global register`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!IsGlobalGenerator(generatorId)) {
```
