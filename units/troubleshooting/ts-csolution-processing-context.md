---
id: "ts-csolution-processing-context"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: processing context"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["processing context '<…>' failed"]
symptom_regex: "^processing context '.+?' failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:743"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`processing context '<…>' failed`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_worker.ProcessContext(contextItem, true, true, false)) {
```
