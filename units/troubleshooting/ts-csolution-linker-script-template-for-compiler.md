---
id: "ts-csolution-linker-script-template-for-compiler"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: linker script template for compiler"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["linker script template for compiler '<…>' was not found"]
symptom_regex: "^linker script template for compiler '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:2462"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`linker script template for compiler '<…>' was not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (linkerScript.empty()) {
```
