---
id: "ts-csolution-csolution-file-was-not-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: csolution file was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["csolution file was not found"]
symptom_regex: "^csolution file was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgr.cpp:271"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The command line named a csolution file, either as a positional argument ending in .csolution.yml or .csolution.yaml or via the --solution option, and that path does not exist on disk when csolution checks it."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:257-268", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:269-271"]
---

## Symptom

`csolution file was not found`

## Cause

The command line named a csolution file, either as a positional argument ending in .csolution.yml or .csolution.yaml or via the --solution option, and that path does not exist on disk when csolution checks it. The message is printed with the given path as its detail, so the user's path is what is missing or mistyped.

## Fix

Check the path given on the command line for typos and make sure it is relative to the current working directory or absolute. Confirm the file exists with its full .csolution.yml or .csolution.yaml name, then run the command again, for example: csolution convert -s path/to/project.csolution.yml

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(m_csolutionFile)) {
```

## Note

The README does not document this message. The check runs before the path is canonicalized, so a relative path is tested against the current working directory. The message is printed with the path as its detail argument, which is why the path appears after the message in the log.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgr.cpp:257-268`
- `tools/projmgr/src/ProjMgr.cpp:269-271`
