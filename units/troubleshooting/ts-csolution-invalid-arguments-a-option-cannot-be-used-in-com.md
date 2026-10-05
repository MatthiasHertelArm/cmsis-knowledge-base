---
id: "ts-csolution-invalid-arguments-a-option-cannot-be-used-in-com"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: invalid arguments: '-a' option cannot be used in combination with '-S"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["invalid arguments: '-a' option cannot be used in combination with '-S'"]
symptom_regex: "^invalid arguments: '\\-a' option cannot be used in combination with '\\-S'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5231"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`invalid arguments: '-a' option cannot be used in combination with '-S'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (checkCbuildSet && !m_activeTargetType.empty()) {
```
