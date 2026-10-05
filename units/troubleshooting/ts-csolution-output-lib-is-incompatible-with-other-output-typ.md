---
id: "ts-csolution-output-lib-is-incompatible-with-other-output-typ"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: output 'lib' is incompatible with other output types"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["output 'lib' is incompatible with other output types"]
symptom_regex: "^output 'lib' is incompatible with other output types$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5611"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`output 'lib' is incompatible with other output types`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (context.outputTypes.lib.on &&
```
