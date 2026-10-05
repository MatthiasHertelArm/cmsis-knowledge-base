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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:570"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:566", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteKernel.cpp:415", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:486", "Open-CMSIS-Pack/devtools@30f5e817:libs/crossplatform/src/CrossPlatformUtils.cpp:37"]
---

## Symptom

`parsing installed packs failed`

## Cause

csolution wanted to load the installed packs (no pack is required by the YAML, or `-l all`/`-l latest` is set) but has no pack root: CMSIS_PACK_ROOT is not set and no default location could be derived from the user environment.

## Fix

Set CMSIS_PACK_ROOT to the pack folder, e.g. `export CMSIS_PACK_ROOT=$HOME/.cache/arm/packs`, and initialise it with `cpackget init` if it does not exist yet.

## Trigger in the source

```cpp
if (!m_kernel->GetEffectivePdscFiles(pdscFiles, latest)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:566`
- `libs/rtemodel/src/RteKernel.cpp:415`
- `tools/projmgr/src/ProjMgrWorker.cpp:486`
- `libs/crossplatform/src/CrossPlatformUtils.cpp:37`
