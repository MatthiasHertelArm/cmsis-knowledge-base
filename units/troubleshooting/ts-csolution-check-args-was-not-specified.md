---
id: "ts-csolution-check-args-was-not-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: check <args> was not specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["check <args> was not specified"]
symptom_regex: "^check <args> was not specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:451"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`check <args> was not specified`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (m_args.empty()) {
```
