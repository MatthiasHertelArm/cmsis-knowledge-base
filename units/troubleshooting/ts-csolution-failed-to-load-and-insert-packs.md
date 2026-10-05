---
id: "ts-csolution-failed-to-load-and-insert-packs"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: failed to load and insert packs"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["failed to load and insert packs"]
symptom_regex: "^failed to load and insert packs$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:575"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:539-577", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteKernel.cpp:465-488", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteKernel.cpp:293-320", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteKernel.cpp:36"]
---

## Symptom

`failed to load and insert packs`

## Cause

A pack description file (*.pdsc) that csolution has to load cannot be read or parsed: an installed pack under CMSIS_PACK_ROOT or a local pack referenced with `packs: - pack: ... path:`. 'Error parsing XML file' messages naming the file follow.

## Fix

Look at the errors that follow to find the failing *.pdsc; reinstall that pack with cpackget (e.g. remove its damaged folder and run `cpackget add Vendor::Name`), or repair the pdsc of the local pack referenced by `path:`.

## Trigger in the source

```cpp
if (!m_kernel->LoadAndInsertPacks(m_loadedPacks, pdscFiles)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:539-577`
- `libs/rtemodel/src/RteKernel.cpp:465-488`
- `libs/rtemodel/src/RteKernel.cpp:293-320`
- `libs/rtemodel/src/RteKernel.cpp:36`
