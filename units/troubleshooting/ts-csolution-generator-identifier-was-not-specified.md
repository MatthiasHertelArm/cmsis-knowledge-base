---
id: "ts-csolution-generator-identifier-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator identifier was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator identifier was not specified"]
symptom_regex: "^generator identifier was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:1045"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`generator identifier was not specified`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (m_codeGenerator.empty()) {
```
