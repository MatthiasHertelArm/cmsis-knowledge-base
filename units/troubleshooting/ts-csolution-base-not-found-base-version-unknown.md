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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2408"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A component configuration file in the RTE folder exists, but its backup `<file>.base@<version>` beside it is missing, so csolution cannot tell from which pack version the file was copied (PLM status 'missing base')."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2385-2411", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:751-773", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteProject.cpp:671-690", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:6958-7004"]
---

## Symptom

`file '<…>.base' not found; base version unknown`

## Cause

A component configuration file in the RTE folder exists, but its backup `<file>.base@<version>` beside it is missing, so csolution cannot tell from which pack version the file was copied (PLM status 'missing base'). Typical when the RTE files were last processed with `--no-update-rte`, by an older tool, or the `*.base@*` files were not committed to version control. The `<…>` is the config file path.

## Fix

Run csolution with RTE update enabled (`csolution update-rte <name>.csolution.yml`, or convert without `--no-update-rte`); it recreates the base backup where it can. Keep the `*.base@*` files under version control together with the RTE folder.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(file + '.' + RteUtils::BASE_STRING + '@' + baseVersion)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2385-2411`
- `tools/projmgr/src/ProjMgr.cpp:751-773`
- `libs/rtemodel/src/RteProject.cpp:671-690`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:6958-7004`
