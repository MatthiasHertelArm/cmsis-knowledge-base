---
id: "ts-csolution-does-not-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: pack path: … does not exist"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["pack path: <…> does not exist"]
symptom_regex: "^pack path: .+? does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:1800"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `packs:` entry has a `path:` to a local pack folder that does not exist; `<…>` is the resolved path."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1800", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1746", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/test_local_pack_path_not_found.csolution.yml:73", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3900"]
---

## Symptom

`pack path: <…> does not exist`

## Cause

A `packs:` entry has a `path:` to a local pack folder that does not exist; `<…>` is the resolved path. The path is relative to the YAML file that holds the entry (csolution.yml, cproject.yml or clayer.yml).

## Fix

Correct `path:` so that it points to the folder that contains the pack's pdsc file, e.g. `- pack: ARM::RteTest_DFP` with `path: ./packs/RteTest_DFP`, or remove `path:` to use the installed pack.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(package.path)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1800`
- `tools/projmgr/src/ProjMgrWorker.cpp:1746`
- `tools/projmgr/test/data/TestSolution/test_local_pack_path_not_found.csolution.yml:73`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3900`
