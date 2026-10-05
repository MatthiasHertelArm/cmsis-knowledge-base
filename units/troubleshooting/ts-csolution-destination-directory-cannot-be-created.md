---
id: "ts-csolution-destination-directory-cannot-be-created"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: destination directory cannot be created"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["destination directory cannot be created"]
symptom_regex: "^destination directory cannot be created$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlEmitter.cpp:61"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`destination directory cannot be created`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteFsUtils::MakeSureFilePath(filename)) {
```
