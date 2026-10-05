---
id: "ts-csolution-missing-rte-target"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: missing RTE target"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["missing RTE target"]
symptom_regex: "^missing RTE target$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1978"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`missing RTE target`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!context.rteActiveTarget) {
```
