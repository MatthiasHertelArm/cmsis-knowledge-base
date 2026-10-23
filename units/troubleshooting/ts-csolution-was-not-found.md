---
id: "ts-csolution-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: board '…' was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["board '<…>' was not found"]
symptom_regex: "^board '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:1372"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The `board:` of the target type (format `[Vendor::]Name[:Revision]`) matches no board in the loaded packs: no board has exactly that name, or the vendor before `::` differs."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1357-1374", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1394-1397", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:559-569", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3116-3150", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:860", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:918"]
---

## Symptom

`board '<…>' was not found`

## Cause

The `board:` of the target type (format `[Vendor::]Name[:Revision]`) matches no board in the loaded packs: no board has exactly that name, or the vendor before `::` differs. Only boards of the packs listed under packs: are searched (all installed packs when none are listed). The `<…>` is the board as written; the same text is printed when name and vendor match but no board has the given `:Revision`.

## Fix

Look up the exact name with `csolution list boards <name>.csolution.yml -f <part-of-name>` and copy it into `board:`; if the board is missing there, add its board support pack under packs: and install it with `cpackget add Vendor::PackName`.

## Trigger in the source

```cpp
if (partialMatchedBoards.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1357-1374`
- `tools/projmgr/src/ProjMgrWorker.cpp:1394-1397`
- `tools/projmgr/src/ProjMgrWorker.cpp:559-569`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3116-3150`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:860`
- `tools/projmgr/test/src/ProjMgrWorkerUnitTests.cpp:918`
