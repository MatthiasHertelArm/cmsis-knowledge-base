---
id: "ts-csolution-file-doesn-t-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file doesn't exist"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["file doesn't exist: '<…>'"]
symptom_regex: "^file doesn't exist: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlSchemaChecker.cpp:22"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`file doesn't exist: '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteFsUtils::Exists(file)) {
```
