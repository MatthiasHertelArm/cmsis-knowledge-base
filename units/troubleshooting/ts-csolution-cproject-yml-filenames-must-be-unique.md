---
id: "ts-csolution-cproject-yml-filenames-must-be-unique"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cproject.yml filenames must be unique"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cproject.yml filenames must be unique"]
symptom_regex: "^cproject\\.yml filenames must be unique$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgr.cpp:517"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "Two entries under projects: of the csolution.yml use the same cproject file name in different folders, e.g. app1/app.cproject.yml and app2/app.cproject.yml."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:508-519", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5010-5025"]
---

## Symptom

`cproject.yml filenames must be unique`

## Cause

Two entries under projects: of the csolution.yml use the same cproject file name in different folders, e.g. app1/app.cproject.yml and app2/app.cproject.yml. The project name, and with it the context names, is taken from the file name, so the names must differ.

## Fix

Rename one of the project files, e.g. app2/app2.cproject.yml, and update its `project:` entry.

## Trigger in the source

```cpp
if (adjacent_find(names.begin(), names.end()) != names.end()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:508-519`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5010-5025`
