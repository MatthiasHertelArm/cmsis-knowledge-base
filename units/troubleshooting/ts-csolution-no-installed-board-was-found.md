---
id: "ts-csolution-no-installed-board-was-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no installed board was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no installed board was found"]
symptom_regex: "^no installed board was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:4293"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`no installed board was found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (boardsSet.empty()) {
```
