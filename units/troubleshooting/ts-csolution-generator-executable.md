---
id: "ts-csolution-generator-executable"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator executable '…' was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator executable '<…>' was not found"]
symptom_regex: "^generator executable '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5147"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The generator with id generatorId was found in the context's generators, but GetExecutable(context.rteActiveTarget) returned an empty path for the active target."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5145-5149", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5112-5114"]
---

## Symptom

`generator executable '<…>' was not found`

## Cause

The generator with id generatorId was found in the context's generators, but GetExecutable(context.rteActiveTarget) returned an empty path for the active target. This means the generator's package definition (PDSC) does not give an executable for the selected target, so there is nothing to check for existence or permissions. The '<…>' in the message is the generator id the user asked to run.

## Fix

Check that the generator entry in the PDSC of the pack that provides it declares an executable for the target in use, and that the pack providing the generator is installed and selected for the context. Then rerun the generator command. The source lines give no further fix beyond this.

## Trigger in the source

```cpp
if (generatorExe.empty()) {
```

## Note

The message text is the same as the one in the code path only when the executable is empty; the message does not name the executable or the target. The condition is read from the lines given; the README entry does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5145-5149`
- `tools/projmgr/src/ProjMgrWorker.cpp:5112-5114`
