---
id: "ts-csolution-manifest-file-does-not-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: manifest file does not exist"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["manifest file does not exist"]
symptom_regex: "^manifest file does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgr.cpp:1215"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`manifest file does not exist`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteFsUtils::FindFileWithPattern(toolboxDir, manifestFilePattern, manifestFile)) {
```
