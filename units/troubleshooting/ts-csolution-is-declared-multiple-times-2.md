---
id: "ts-csolution-is-declared-multiple-times-2"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is declared multiple times"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["conflict: file '<…>' is declared multiple times"]
symptom_regex: "^conflict: file '.+?' is declared multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3854"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`conflict: file '<…>' is declared multiple times`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (dstNode.file == src.file) {
```
