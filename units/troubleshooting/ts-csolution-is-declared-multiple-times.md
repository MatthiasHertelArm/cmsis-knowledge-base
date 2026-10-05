---
id: "ts-csolution-is-declared-multiple-times"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is declared multiple times"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["conflict: group '<…>' is declared multiple times"]
symptom_regex: "^conflict: group '.+?' is declared multiple times$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3835"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`conflict: group '<…>' is declared multiple times`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (dstNode.group == src.group) {
```
