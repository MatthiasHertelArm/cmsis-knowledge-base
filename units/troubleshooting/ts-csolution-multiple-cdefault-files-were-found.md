---
id: "ts-csolution-multiple-cdefault-files-were-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: multiple cdefault files were found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["multiple cdefault files were found"]
symptom_regex: "^multiple cdefault files were found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:1164"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`multiple cdefault files were found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!cdefaultFile.empty()) {
```
