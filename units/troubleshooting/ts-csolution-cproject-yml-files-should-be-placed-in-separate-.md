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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:521"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution file lists more than one cproject, and two or more of them have the same parent directory, so their cproject.yml files are not in separate sub-directories."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:508-523", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:513", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:520-521"]
---

## Symptom

`cproject.yml files should be placed in separate sub-directories`

## Cause

The csolution file lists more than one cproject, and two or more of them have the same parent directory, so their cproject.yml files are not in separate sub-directories. The check sorts the parent directories of all listed cprojects into a multiset and warns when any directory appears twice. This is a warning only, so processing continues.

## Fix

Move each cproject.yml into its own sub-directory, so that every project's parent directory is distinct, and update the cprojects entries in the csolution.yml to match. Keeping the same directory and only renaming the file does not clear it, because the check compares directories.

## Trigger in the source

```cpp
if (adjacent_find(dirs.begin(), dirs.end()) != dirs.end()) {
```

## Note

Unlike the duplicate filename check at line 516, which is an error, this directory check only warns and the function continues. Duplicate directories are reached only when cprojects.size() is greater than one.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:508-523`
- `tools/projmgr/src/ProjMgr.cpp:513`
- `tools/projmgr/src/ProjMgr.cpp:520-521`
