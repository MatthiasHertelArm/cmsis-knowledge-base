---
id: "ts-csolution-not-found-in-included-packs"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: not found in included packs"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["component '<…>' not found in included packs<…>\n  did you mean '<…>'?<…>"]
symptom_regex: "^component '.+?' not found in included packs.+?\\\n  did you mean '.+?'\\?.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:2001"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`component '<…>' not found in included packs<…>
  did you mean '<…>'?<…>`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!matchedComponent) {
```
