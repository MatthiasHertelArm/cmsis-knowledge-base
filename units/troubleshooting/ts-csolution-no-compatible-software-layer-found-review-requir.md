---
id: "ts-csolution-no-compatible-software-layer-found-review-requir"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no compatible software layer found. Review required connections of the"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no compatible software layer found. Review required connections of the project"]
symptom_regex: "^no compatible software layer found\\. Review required connections of the project$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:1016"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no compatible software layer found. Review required connections of the project`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_worker.ListLayers(layers, m_clayerSearchPath, m_failedContext)) {
```
