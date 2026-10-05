---
id: "ts-csolution-board-mounted-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: board mounted device"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["board mounted device <…> not found"]
symptom_regex: "^board mounted device .+? not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:1446"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`board mounted device <…> not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!device) {
```
