---
id: "ts-csolution-multiple-linker-scripts-defined"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: ; multiple linker scripts defined"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' this linker script is ignored<…>; multiple linker scripts defined<…>"]
symptom_regex: "^'.+?' this linker script is ignored.+?; multiple linker scripts defined.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:3884"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`'<…>' this linker script is ignored<…>; multiple linker scripts defined<…>`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!context.linker.autoGen && context.linker.script.empty() &&
```
