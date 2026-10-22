---
id: "ts-csolution-file-cannot-be-written"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: file cannot be written"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["file cannot be written"]
symptom_regex: "^file cannot be written$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:802"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "During RunConvert, csolution builds the output path <cprj directory>/<context name>.cprj and calls m_generator.GenerateCprj for it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:795-804", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:797-798"]
---

## Symptom

`file cannot be written`

## Cause

During RunConvert, csolution builds the output path <cprj directory>/<context name>.cprj and calls m_generator.GenerateCprj for it. When that call returns false, the tool prints this error with the context name and file path and stops. The source does not show the underlying write error, and the result of RteFsUtils::CreateDirectories on the cprj directory is ignored, so a missing or unwritable output directory, or a path that cannot be created, is a likely reason.

## Fix

Check that the cprj output directory exists or can be created, is not blocked by a file of the same name, and is writable by the current user. Confirm the path printed in the message is valid, then rerun csolution. If the directory is fine, the source gives no further step; check the permissions and disk space of the printed path.

## Trigger in the source

```cpp
if (m_generator.GenerateCprj(*contextItem, filename)) {
```

## Note

The message is printed only when GenerateCprj returns false, and the generator's reason is not logged in these lines. The cause given is an inference from the directory creation and path setup around the trigger, not a confirmed failure mode. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:795-804`
- `tools/projmgr/src/ProjMgr.cpp:797-798`
