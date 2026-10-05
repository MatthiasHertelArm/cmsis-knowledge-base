---
id: "ts-csolution-input-csolution-yml-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: input csolution.yml was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["input csolution.yml was not specified"]
symptom_regex: "^input csolution\\.yml was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:1076"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`input csolution.yml was not specified`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (m_csolutionFile.empty()) {
```
