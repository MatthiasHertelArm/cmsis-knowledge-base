---
id: "ts-csolution-is-not-among-board-mounted-devices"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is not among board mounted devices"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["specified device '<…>' is not among board mounted devices"]
symptom_regex: "^specified device '.+?' is not among board mounted devices$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1490"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`specified device '<…>' is not among board mounted devices`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!match) {
```
