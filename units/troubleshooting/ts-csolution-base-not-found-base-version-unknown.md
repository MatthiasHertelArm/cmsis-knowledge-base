---
id: "ts-csolution-base-not-found-base-version-unknown"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: .base' not found; base version unknown"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["file '<…>.base' not found; base version unknown"]
symptom_regex: "^file '.+?\\.base' not found; base version unknown$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:2408"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`file '<…>.base' not found; base version unknown`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!RteFsUtils::Exists(file + '.' + RteUtils::BASE_STRING + '@' + baseVersion)) {
```
