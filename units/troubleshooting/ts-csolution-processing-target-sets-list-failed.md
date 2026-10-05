---
id: "ts-csolution-processing-target-sets-list-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processing target-sets list failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processing target-sets list failed"]
symptom_regex: "^processing target\\-sets list failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:926"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`processing target-sets list failed`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_worker.ListTargetSets(targetSets, m_filter)) {
```
