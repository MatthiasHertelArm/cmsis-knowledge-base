---
id: "ts-csolution-target-types-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: target-types not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["target-types not found"]
symptom_regex: "^target\\-types not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:95"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`target-types not found`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!ParseTargetTypes(solutionNode, csolution.path, csolution.targetTypes)) {
```
