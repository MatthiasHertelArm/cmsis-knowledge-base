---
id: "ts-csolution-required-packs-must-be-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: required packs must be specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["required packs must be specified"]
symptom_regex: "^required packs must be specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:563"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution was run with `-l required` (`--load required`), which loads only the packs the project names, but the selected contexts name none: there is no `packs:` entry in the csolution.yml, cproject.yml or clayer.yml and no cbuild-pack.yml with resolved packs."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:561", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:543", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1837", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3973"]
---

## Symptom

`required packs must be specified`

## Cause

csolution was run with `-l required` (`--load required`), which loads only the packs the project names, but the selected contexts name none: there is no `packs:` entry in the csolution.yml, cproject.yml or clayer.yml and no cbuild-pack.yml with resolved packs.

## Fix

List the packs under `packs:` in the csolution.yml, e.g. `- pack: ARM::CMSIS` and `- pack: Keil::STM32U5xx_DFP`, or run without `-l required` so that csolution uses the installed packs.

## Trigger in the source

```cpp
if (noPackRequirements && (m_loadPacksPolicy == LoadPacksPolicy::REQUIRED)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:561`
- `tools/projmgr/src/ProjMgrWorker.cpp:543`
- `tools/projmgr/src/ProjMgrWorker.cpp:1837`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3973`
