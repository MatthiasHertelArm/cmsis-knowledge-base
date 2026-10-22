---
id: "ts-csolution-cannot-be-executed-check-permissions"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator file '…' cannot be executed, check permissions"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator file '<…>' cannot be executed, check permissions"]
symptom_regex: "^generator file '.+?' cannot be executed, check permissions$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5156"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The generator executable path resolved for the active target exists on disk, but RteFsUtils::IsExecutableFile reports it is not executable by the current user."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5145-5146", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5150-5153", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5155-5157"]
---

## Symptom

`generator file '<…>' cannot be executed, check permissions`

## Cause

The generator executable path resolved for the active target exists on disk, but RteFsUtils::IsExecutableFile reports it is not executable by the current user. The path is the generator's executable as resolved in ExecuteGenerator via generator->GetExecutable(context.rteActiveTarget); the check runs after the existence check, so the file is present but lacks execute permission.

## Fix

Check the file's permissions on the reported path (for example with ls -l) and make it executable for the current user, e.g. chmod +x on that file, then rerun the generator command. If the file came from a pack, reinstall or re-extract the pack so the executable bit is restored.

## Trigger in the source

```cpp
if (!RteFsUtils::IsExecutableFile(generatorExe)) {
```

## Note

The message is not documented in the README. The cause is inferred from the existence check preceding this one; the source does not show how IsExecutableFile determines executability, so a filesystem or platform-specific reason (such as a non-executable file type) is not excluded by the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5145-5146`
- `tools/projmgr/src/ProjMgrWorker.cpp:5150-5153`
- `tools/projmgr/src/ProjMgrWorker.cpp:5155-5157`
