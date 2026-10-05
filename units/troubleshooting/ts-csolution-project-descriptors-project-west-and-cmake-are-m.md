---
id: "ts-csolution-project-descriptors-project-west-and-cmake-are-m"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: project descriptors 'project', 'west', and 'cmake' are mutually exclus"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["project descriptors 'project', 'west', and 'cmake' are mutually exclusive"]
symptom_regex: "^project descriptors 'project', 'west', and 'cmake' are mutually exclusive$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:885"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`project descriptors 'project', 'west', and 'cmake' are mutually exclusive`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (descriptorCount > 1) {
```
