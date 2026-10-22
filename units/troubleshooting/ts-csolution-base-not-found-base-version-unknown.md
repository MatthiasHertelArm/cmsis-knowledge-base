---
id: "ts-csolution-base-not-found-base-version-unknown"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file '….base' not found; base version unknown"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["file '<…>.base' not found; base version unknown"]
symptom_regex: "^file '.+?\\.base' not found; base version unknown$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2408"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "During the PLM (Pack Lifecycle Management) check, csolution has found the component file instance in the project directory, but the copy of that file's base version, named with the suffix .base@<version> where <version> is the file's semantic version from …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2406-2409", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2394-2399"]
---

## Symptom

`file '<…>.base' not found; base version unknown`

## Cause

During the PLM (Pack Lifecycle Management) check, csolution has found the component file instance in the project directory, but the copy of that file's base version, named with the suffix .base@<version> where <version> is the file's semantic version from the RTE, is not there. The message prints the instance path followed by '.base' without the version suffix that the existence check actually tests. The check sets the file's PLM status to missing base and continues, so the build is not stopped.

## Fix

Restore the missing base copy next to the file instance, or let csolution recreate the RTE-managed files by running the command with --update-rte, then rebuild. The source does not show a separate option for the base copy, so if the message persists after --update-rte, check that the file instance and its version in the pack are consistent.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(file + '.' + RteUtils::BASE_STRING + '@' + baseVersion)) {
```

## Note

The message text omits the @<version> part that the existence check at line 2407 tests, so the file named in the log is not the exact path checked. The --update-rte hint comes from the missing-instance message at line 2394, not from this warning; that the same fix applies here is my reading. This is a warning, not an error.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2406-2409`
- `tools/projmgr/src/ProjMgrWorker.cpp:2394-2399`
