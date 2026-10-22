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
summary: "During LoadAllRelevantPacks, csolution compares each loaded pack's version suffix (the part after '+' in its version string) with the metadata value recorded for that pack ID in m_packMetadata."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:586-593"]
---

## Symptom

`loaded pack '<…>' does not match specified metadata '<…>'`

## Cause

During LoadAllRelevantPacks, csolution compares each loaded pack's version suffix (the part after '+' in its version string) with the metadata value recorded for that pack ID in m_packMetadata. When the two differ, it prints this warning, with the first placeholder being the pack ID plus its version and the second being the metadata value the user's input specified. The warning is only raised when the pack ID has a metadata entry, so the user's input must have supplied a metadata value for that pack, and the installed or loaded pack carries a different '+' suffix.

## Fix

Check the pack version and metadata specified for that pack in the csolution project against the pack actually installed. Either align the pack's version (the '+' suffix) with the specified metadata, for example by installing the matching pack version, or update the metadata in the project to the version suffix that is actually loaded. The source does not show a further automatic resolution, so this is a manual correction.

## Trigger in the source

```cpp
if ((m_packMetadata.find(loadedPackID) != m_packMetadata.end()) &&
```

## Note

The message is a warning and the function still returns true, so processing continues. The first placeholder is built by concatenating GetPackageID(false) and GetVersionString() without a separator, so the printed pack name and version may run together. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:586-593`
