---
id: "ts-csolution-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["board '<…>' was not found"]
symptom_regex: "^board '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1372"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`board '<…>' was not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (partialMatchedBoards.empty()) {
```
