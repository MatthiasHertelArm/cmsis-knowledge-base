---
id: "ts-csolution-a-single-context-must-be-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: a single context must be specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["a single context must be specified"]
symptom_regex: "^a single context must be specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5103"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`a single context must be specified`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (m_selectedContexts.size() != 1) {
```
