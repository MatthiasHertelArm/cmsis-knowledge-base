---
id: "ts-csolution-generator-executable-file"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator executable file"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator executable file '<…>' does not exist"]
symptom_regex: "^generator executable file '.+?' does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5151"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`generator executable file '<…>' does not exist`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if(!RteFsUtils::Exists(generatorExe)) {
```
