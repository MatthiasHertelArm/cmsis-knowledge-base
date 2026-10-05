---
id: "ts-csolution-cgen-file-was-not-found-run-generator"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cgen file was not found, run generator"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cgen file was not found, run generator '<…>' for context '<…>'"]
symptom_regex: "^cgen file was not found, run generator '.+?' for context '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrExtGenerator.cpp:80"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`cgen file was not found, run generator '<…>' for context '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_parser->ParseClayer(options.name, m_checkSchema)) {
```
