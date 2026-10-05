---
id: "ts-csolution-missing-device-and-or-board-info"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: missing device and/or board info"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["missing device and/or board info"]
symptom_regex: "^missing device and/or board info$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1351"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`missing device and/or board info`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (context.board.empty() && deviceItem.name.empty()) {
```
