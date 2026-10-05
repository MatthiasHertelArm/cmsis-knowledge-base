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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6209"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution check pack-updates` with `-f <words>` found packs, but no result line (`Vendor::Pack@version -> newer` or `(up-to-date)`) contains all the filter words; `<…>` is the filter."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:6209", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:1089"]
---

## Symptom

`no packs were found for version check with filter '<…>'`

## Cause

`csolution check pack-updates` with `-f <words>` found packs, but no result line (`Vendor::Pack@version -> newer` or `(up-to-date)`) contains all the filter words; `<…>` is the filter.

## Fix

Loosen the filter, e.g. the pack name only, or run the check without `-f`.

## Trigger in the source

```cpp
if (matchedPacks.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:6209`
- `tools/projmgr/src/ProjMgr.cpp:1089`
