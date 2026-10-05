---
id: "ts-csolution-duplicate-cmake-image-type"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: duplicate CMake image type"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["duplicate CMake image type '<…>'"]
symptom_regex: "^duplicate CMake image type '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:927"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`duplicate CMake image type '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!imageTypes.insert(image.type).second) {
```
