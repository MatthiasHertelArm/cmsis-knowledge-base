---
id: "ts-csolution-no-packs-were-found-for-version-check-with-filte"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no packs were found for version check with filter '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no packs were found for version check with filter '<…>'"]
symptom_regex: "^no packs were found for version check with filter '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:6209"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The version check ran and produced one or more pack result lines, but the filter given on the command line matched none of them."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6205-6211", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6170-6182", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6199"]
---

## Symptom

`no packs were found for version check with filter '<…>'`

## Cause

The version check ran and produced one or more pack result lines, but the filter given on the command line matched none of them. The filter is split into a set of terms and applied to each result line (packId@version, with the up-to-date or outdated status), and the '<…>' in the message is the filter string the user passed.

## Fix

Check the filter text against the pack result lines the check prints without a filter. Use a term that appears in those lines, such as a vendor::pack name or part of a version string, or drop the filter to see every result.

## Trigger in the source

```cpp
if (matchedPacks.empty()) {
```

## Note

The README does not document this message. The reading of the filter term format is inferred from the ApplyFilter and SplitStringToSet calls; the exact matching rules are in RteUtils and were not in the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:6205-6211`
- `tools/projmgr/src/ProjMgrWorker.cpp:6170-6182`
- `tools/projmgr/src/ProjMgrWorker.cpp:6199`
