---
id: "ts-csolution-parsing-installed-packs-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: parsing installed packs failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["parsing installed packs failed"]
symptom_regex: "^parsing installed packs failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:570"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`parsing installed packs failed`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (!m_kernel->GetEffectivePdscFiles(pdscFiles, latest)) {
```
