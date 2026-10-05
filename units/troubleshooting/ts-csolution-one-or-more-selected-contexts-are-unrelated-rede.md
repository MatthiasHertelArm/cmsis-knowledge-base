---
id: "ts-csolution-one-or-more-selected-contexts-are-unrelated-rede"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: one or more selected contexts are unrelated, redefine the '--context a"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["one or more selected contexts are unrelated, redefine the '--context arg [...]' option"]
symptom_regex: "^one or more selected contexts are unrelated, redefine the '\\-\\-context arg \\[\\.\\.\\.\\]' option$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/projmgr/src/ProjMgrWorker.cpp:5870"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`one or more selected contexts are unrelated, redefine the '--context arg [...]' option`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_

## Trigger im Quelltext

```cpp
if (find(siblingProjects.begin(), siblingProjects.end(), selectedContextItem->cproject->name) == siblingProjects.end()) {
```
