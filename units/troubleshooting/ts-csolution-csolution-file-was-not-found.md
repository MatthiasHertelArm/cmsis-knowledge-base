---
id: "ts-csolution-csolution-file-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: csolution file was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["csolution file was not found"]
symptom_regex: "^csolution file was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:271"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`csolution file was not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteFsUtils::Exists(m_csolutionFile)) {
```
