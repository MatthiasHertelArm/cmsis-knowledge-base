---
id: "ts-csolution-cannot-be-executed-check-permissions"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cannot be executed, check permissions"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator file '<…>' cannot be executed, check permissions"]
symptom_regex: "^generator file '.+?' cannot be executed, check permissions$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5156"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`generator file '<…>' cannot be executed, check permissions`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteFsUtils::IsExecutableFile(generatorExe)) {
```
