---
id: "ts-csolution-too-many-command-line-arguments"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: too many command line arguments"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["too many command line arguments"]
symptom_regex: "^too many command line arguments$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:322"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`too many command line arguments`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!parseResult.unmatched().empty()) {
```
