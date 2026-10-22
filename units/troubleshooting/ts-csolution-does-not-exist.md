---
id: "ts-csolution-does-not-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: pack path: … does not exist"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["pack path: <…> does not exist"]
symptom_regex: "^pack path: .+? does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1800"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A pack entry in the csolution project files has a `path` that points to a local pack folder, and that path does not exist once it is resolved against the csolution file's directory."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1794-1802", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1796-1800", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1804-1809"]
---

## Symptom

`pack path: <…> does not exist`

## Cause

A pack entry in the csolution project files has a `path` that points to a local pack folder, and that path does not exist once it is resolved against the csolution file's directory. The message prints the path exactly as written in the project file (`packageEntry.path`), so `<…>` is that raw value. The check runs on the normalized copy, so a relative path is judged from the csolution directory, not from the current working directory.

## Fix

Open the csolution or project file that lists the pack and find the `path` value named in the message. Make it relative to that file's directory, or use an absolute path, so that it points to the folder that contains the pack's .pdsc file. Confirm the folder exists on disk, then run the build again. The folder must also contain `<vendor>.<name>.pdsc`, or the tool stops with a different error about a missing pdsc file.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(package.path)) {
```

## Note

The message is not documented in the README. The printed path is the unresolved value from the project file, not the resolved absolute path that was tested, so the user has to resolve it relative to the csolution directory to see what the tool checked. The code field is empty in the catalog entry.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1794-1802`
- `tools/projmgr/src/ProjMgrWorker.cpp:1796-1800`
- `tools/projmgr/src/ProjMgrWorker.cpp:1804-1809`
