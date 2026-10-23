---
id: "ts-csolution-missing-device-and-or-board-info"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: missing device and/or board info"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["missing device and/or board info"]
symptom_regex: "^missing device and/or board info$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:1351"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The context has neither a `board:` nor a device name in `device:` at any level (target-types in the csolution.yml, the cproject.yml or a clayer.yml)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1347", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:774", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3065", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3098"]
---

## Symptom

`missing device and/or board info`

## Cause

The context has neither a `board:` nor a device name in `device:` at any level (target-types in the csolution.yml, the cproject.yml or a clayer.yml). A `device:` with only a processor name, such as `device: :cm0_core0`, does not count.

## Fix

Add a board or a device to the target type in the csolution.yml, e.g. `target-types:` - `type: CM0` with `device: ARMCM0` or `board: <vendor>::<board name>`.

## Trigger in the source

```cpp
if (context.board.empty() && deviceItem.name.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1347`
- `tools/projmgr/src/ProjMgrWorker.cpp:774`
- `tools/projmgr/src/ProjMgrWorker.cpp:3065`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3098`
