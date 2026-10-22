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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:6147"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The pack version check (CheckPackVerAndCollectRelNotes) asks the kernel to build a map of the latest available version and PDSC path for each pack from the pack index."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6146-6149"]
---

## Symptom

`failed to read latest pack information from pack index`

## Cause

The pack version check (CheckPackVerAndCollectRelNotes) asks the kernel to build a map of the latest available version and PDSC path for each pack from the pack index. ReadPackLatestVerAndPath returned false, so the check stops before it reads any project packs. The lines shown do not include ReadPackLatestVerAndPath, so the specific reason it failed (missing or unreadable pack index, pack root not set up) is not visible here.

## Fix

Check that the CMSIS pack root has a readable pack index, meaning the .Index files and the .pdsc files they reference are present and not corrupted. If the index is missing or stale, refresh the installed packs with the CMSIS pack tooling (for example cpackget update-index or cpackget add for the needed packs) and run the check again. The source lines given do not show which index file or path the kernel reads, so confirm that location in ReadPackLatestVerAndPath before going further.

## Trigger in the source

```cpp
if (!m_kernel->ReadPackLatestVerAndPath(latestPacks)) {
```

## Note

The message is printed only when ReadPackLatestVerAndPath returns false; the reason it fails is in code not shown. The README does not document this message. The fix about cpackget commands is a general suggestion and is not confirmed by the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:6146-6149`
