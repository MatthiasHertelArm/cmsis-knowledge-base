---
id: "ts-csolution-is-not-selectable-as-active-target-set"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is not selectable as active target-set"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["'<…>' is not selectable as active target-set"]
symptom_regex: "^'.+?' is not selectable as active target\\-set$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:6321"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`'<…>' is not selectable as active target-set`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (m_activeTargetType.empty() || (!targetSetFound && !targetSet.empty())) {
```
