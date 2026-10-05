---
id: "ts-csolution-projects-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: projects not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["projects not found"]
symptom_regex: "^projects not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:505"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`projects not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!IsSolutionImageOnly() && cprojects.empty() && m_parser.GetCsolution().westApps.empty() && m_parser.GetCsolution().cmakeApps.empty()) {
```
