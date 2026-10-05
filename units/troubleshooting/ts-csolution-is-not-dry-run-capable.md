---
id: "ts-csolution-is-not-dry-run-capable"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is not dry-run capable"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator '<…>' is not dry-run capable"]
symptom_regex: "^generator '.+?' is not dry\\-run capable$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5160"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`generator '<…>' is not dry-run capable`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (m_dryRun && !generator->IsDryRunCapable(generatorExe)) {
```
