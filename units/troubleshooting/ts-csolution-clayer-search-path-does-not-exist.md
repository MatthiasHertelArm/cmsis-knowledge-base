---
id: "ts-csolution-clayer-search-path-does-not-exist"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: clayer search path does not exist"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["clayer search path does not exist"]
symptom_regex: "^clayer search path does not exist$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:862"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:857-864", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:301-303", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:2459-2467"]
---

## Symptom

`clayer search path does not exist`

## Cause

The folder given with `--clayer-path`/`-L` to `csolution list layers` does not exist. A relative path is resolved against the current working directory, not against the csolution.yml; the message is prefixed with the resolved path.

## Fix

Pass an existing folder, e.g. `csolution list layers <name>.csolution.yml -L ./layers` from the folder that contains it, or an absolute path.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(absSearchPath)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:857-864`
- `tools/projmgr/src/ProjMgr.cpp:301-303`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:2459-2467`
