---
id: "ts-csolution-conflict-automatic-linker-script-generation-over"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: conflict: automatic linker script generation overrules specified scrip"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["conflict: automatic linker script generation overrules specified script '<…>'"]
symptom_regex: "^conflict: automatic linker script generation overrules specified script '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:2359"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`conflict: automatic linker script generation overrules specified script '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!context.linker.script.empty()) {
```
