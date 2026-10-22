---
id: "ts-csolution-does-not-match-specified-metadata"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: loaded pack '…' does not match specified metadata '…'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["loaded pack '<…>' does not match specified metadata '<…>'"]
symptom_regex: "^loaded pack '.+?' does not match specified metadata '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:590"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `packs:` entry pins a version with build metadata, such as `- pack: ARM::RteTest_DFP@0.1.1+user_metadata`, but the installed pack of that version carries different metadata after the `+` in its release version."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:586", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1779", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/PackMetadata/metadata.csolution.yml:18", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:6345"]
---

## Symptom

`loaded pack '<…>' does not match specified metadata '<…>'`

## Cause

A `packs:` entry pins a version with build metadata, such as `- pack: ARM::RteTest_DFP@0.1.1+user_metadata`, but the installed pack of that version carries different metadata after the `+` in its release version. The first `<…>` is the loaded pack (printed without the `@` before the version), the second the metadata from the YAML. The pack is still used.

## Fix

Make the `+<metadata>` suffix in the `packs:` entry match the installed pack, or drop the suffix: `- pack: ARM::RteTest_DFP@0.1.1`.

## Trigger in the source

```cpp
if ((m_packMetadata.find(loadedPackID) != m_packMetadata.end()) &&
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:586`
- `tools/projmgr/src/ProjMgrWorker.cpp:1779`
- `tools/projmgr/test/data/TestSolution/PackMetadata/metadata.csolution.yml:18`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:6345`
