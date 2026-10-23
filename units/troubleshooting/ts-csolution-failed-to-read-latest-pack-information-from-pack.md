---
id: "ts-csolution-failed-to-read-latest-pack-information-from-pack"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: failed to read latest pack information from pack index"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["failed to read latest pack information from pack index"]
symptom_regex: "^failed to read latest pack information from pack index$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:6147"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution check pack-updates` found no pack information at all: the pack index $CMSIS_PACK_ROOT/.Web/index.pidx is missing or unreadable, and no installed or local pack could be read either."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6137-6149", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteKernel.cpp:610-678", "Open-CMSIS-Pack/devtools@30f5e817:tools/buildmgr/test/scripts/setup_test.sh:131-133"]
---

## Symptom

`failed to read latest pack information from pack index`

## Cause

`csolution check pack-updates` found no pack information at all: the pack index $CMSIS_PACK_ROOT/.Web/index.pidx is missing or unreadable, and no installed or local pack could be read either. Usually CMSIS_PACK_ROOT points to an empty or uninitialized pack root.

## Fix

Initialize the pack root with `cpackget init https://www.keil.com/pack/index.pidx` or refresh an existing one with `cpackget update-index`, and check that CMSIS_PACK_ROOT points to it.

## Trigger in the source

```cpp
if (!m_kernel->ReadPackLatestVerAndPath(latestPacks)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:6137-6149`
- `libs/rtemodel/src/RteKernel.cpp:610-678`
- `tools/buildmgr/test/scripts/setup_test.sh:131-133`
