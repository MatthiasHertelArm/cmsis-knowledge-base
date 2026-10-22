---
id: "ts-csolution-generator-executable-file"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator executable file '…' does not exist"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator executable file '<…>' does not exist"]
symptom_regex: "^generator executable file '.+?' does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5151"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution run selected a generator whose executable path, resolved for the active target, is not present on disk."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5145-5146", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5150-5153"]
---

## Symptom

`generator executable file '<…>' does not exist`

## Cause

The csolution run selected a generator whose executable path, resolved for the active target, is not present on disk. The generator comes from a pack's generator definition, and the path printed is the value of generator->GetExecutable(context.rteActiveTarget); the check runs after the cbuild generation step and before the executable permission check.

## Fix

Check that the generator's executable is installed in the pack cache: confirm the pack providing the generator is installed (for example with cpackget or by re-running the csolution command so the required packs are fetched), and that the path printed in the message exists. If the path points into a pack, make sure the pack version in the csolution project matches an installed pack version.

## Trigger in the source

```cpp
if(!RteFsUtils::Exists(generatorExe)) {
```

## Note

The source only shows that the path is missing; the reason it is missing (uninstalled pack, wrong version, wrong target) is inferred. The adjacent message at line 5147 covers the case where no executable path is resolved at all.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5145-5146`
- `tools/projmgr/src/ProjMgrWorker.cpp:5150-5153`
