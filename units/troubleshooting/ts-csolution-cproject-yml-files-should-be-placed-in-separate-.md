---
id: "ts-csolution-cproject-yml-files-should-be-placed-in-separate-"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject.yml files should be placed in separate sub-directories"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["cproject.yml files should be placed in separate sub-directories"]
symptom_regex: "^cproject\\.yml files should be placed in separate sub\\-directories$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgr.cpp:521"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Two or more projects under projects: of the csolution.yml are in the same folder."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:508-523", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:199", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:4992-5007"]
---

## Symptom

`cproject.yml files should be placed in separate sub-directories`

## Cause

Two or more projects under projects: of the csolution.yml are in the same folder. Projects in one folder share that folder's RTE directory and other per-project outputs.

## Fix

Give each cproject.yml (with its sources) its own folder, e.g. app/app.cproject.yml and boot/boot.cproject.yml, and update the `project:` paths.

## Trigger in the source

```cpp
if (adjacent_find(dirs.begin(), dirs.end()) != dirs.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:508-523`
- `tools/projmgr/src/ProjMgrWorker.cpp:199`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:4992-5007`
