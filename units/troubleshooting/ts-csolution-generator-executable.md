---
id: "ts-csolution-generator-executable"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator executable"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator executable '<…>' was not found"]
symptom_regex: "^generator executable '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5147"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`generator executable '<…>' was not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (generatorExe.empty()) {
```
