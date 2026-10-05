---
id: "ts-csolution-is-not-portable-use-relative-path-instead"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: is not portable, use relative path instead"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["absolute path '<…>' is not portable, use relative path instead"]
symptom_regex: "^absolute path '.+?' is not portable, use relative path instead$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrYamlParser.cpp:339"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`absolute path '<…>' is not portable, use relative path instead`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (fs::path(value).is_absolute()) {
```
