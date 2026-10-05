---
id: "ts-csolution-telnet-pname-is-required-multicore-device"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: telnet:' pname is required (multicore device)"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'telnet:' pname is required (multicore device)"]
symptom_regex: "^'telnet:' pname is required \\(multicore device\\)$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrRunDebug.cpp:492"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`'telnet:' pname is required (multicore device)`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (pnames.size() > 1 && value.pname.empty()) {
```
