---
id: "ts-csolution-command-line-options-quiet-and-verbose-are-mutua"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: command line options '--quiet' and '--verbose' are mutually exclusive"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["command line options '--quiet' and '--verbose' are mutually exclusive"]
symptom_regex: "^command line options '\\-\\-quiet' and '\\-\\-verbose' are mutually exclusive$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:332"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`command line options '--quiet' and '--verbose' are mutually exclusive`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (ProjMgrLogger::m_quiet && ProjMgrLogger::m_verbose) {
```
