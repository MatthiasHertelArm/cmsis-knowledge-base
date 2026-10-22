---
id: "ts-csolution-one-or-more-selected-contexts-are-unrelated-rede"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: one or more selected contexts are unrelated, redefine the '--context arg [...]' option"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["one or more selected contexts are unrelated, redefine the '--context arg [...]' option"]
symptom_regex: "^one or more selected contexts are unrelated, redefine the '\\-\\-context arg \\[\\.\\.\\.\\]' option$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5870"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution run -g <generator>` was called with a context selection that spans contexts the generator cannot serve in one call."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5850", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5866", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5812", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5891"]
---

## Symptom

`one or more selected contexts are unrelated, redefine the '--context arg [...]' option`

## Cause

`csolution run -g <generator>` was called with a context selection that spans contexts the generator cannot serve in one call. A global generator runs for one group of sibling contexts (same generator and generator folder, same device, classified as single-core, multi-core or TrustZone), and a selected context whose project is outside that group is unrelated; the context is named with the message.

## Fix

Run the generator once per group: narrow `-c`/`--context` to the contexts of one device and generator (e.g. `-c +MultiCore`), or use `-S` with a cbuild-set.yml that holds such a selection.

## Trigger in the source

```cpp
if (find(siblingProjects.begin(), siblingProjects.end(), selectedContextItem->cproject->name) == siblingProjects.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5850`
- `tools/projmgr/src/ProjMgrWorker.cpp:5866`
- `tools/projmgr/src/ProjMgrWorker.cpp:5812`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5891`
