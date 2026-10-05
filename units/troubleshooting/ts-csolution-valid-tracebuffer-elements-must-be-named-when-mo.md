---
id: "ts-csolution-valid-tracebuffer-elements-must-be-named-when-mo"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: valid <tracebuffer> elements must be named when more than one is decla"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["valid <tracebuffer> elements must be named when more than one is declared"]
symptom_regex: "^valid <tracebuffer> elements must be named when more than one is declared$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrRunDebug.cpp:608"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`valid <tracebuffer> elements must be named when more than one is declared`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (traceBufferCount > 1 && unnamedTraceBufferCount > 0) {
```
