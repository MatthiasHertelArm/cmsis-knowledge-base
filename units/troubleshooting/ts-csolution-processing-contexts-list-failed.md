---
id: "ts-csolution-processing-contexts-list-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processing contexts list failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processing contexts list failed"]
symptom_regex: "^processing contexts list failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:910"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`processing contexts list failed`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_worker.ListContexts(contexts, m_filter, m_ymlOrder)) {
```
