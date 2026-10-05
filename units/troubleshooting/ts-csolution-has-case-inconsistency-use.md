---
id: "ts-csolution-has-case-inconsistency-use"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: has case inconsistency, use"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'<…>' has case inconsistency, use '<…>' instead"]
symptom_regex: "^'.+?' has case inconsistency, use '.+?' instead$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:347"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`'<…>' has case inconsistency, use '<…>' instead`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!canonical.empty() && (original != canonical)) {
```
