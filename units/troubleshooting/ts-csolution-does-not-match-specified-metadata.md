---
id: "ts-csolution-does-not-match-specified-metadata"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: does not match specified metadata"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["loaded pack '<…>' does not match specified metadata '<…>'"]
symptom_regex: "^loaded pack '.+?' does not match specified metadata '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:590"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`loaded pack '<…>' does not match specified metadata '<…>'`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if ((m_packMetadata.find(loadedPackID) != m_packMetadata.end()) &&
```
