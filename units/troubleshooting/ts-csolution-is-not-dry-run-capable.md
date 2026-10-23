---
id: "ts-csolution-is-not-dry-run-capable"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator '…' is not dry-run capable"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator '<…>' is not dry-run capable"]
symptom_regex: "^generator '.+?' is not dry\\-run capable$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:5160"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "`csolution run --dry-run` was used with a pack generator whose `<exe>` in the pack declares no `<argument mode=\"dry-run\">`, so it cannot run without writing files."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5159-5162", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteGenerator.cpp:307-319", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrGeneratorUnitTests.cpp:151-166", "Open-CMSIS-Pack/devtools@30f5e817:test/packs/ARM/RteTestGenerator/0.1.0/ARM.RteTestGenerator.pdsc:110-130"]
---

## Symptom

`generator '<…>' is not dry-run capable`

## Cause

`csolution run --dry-run` was used with a pack generator whose `<exe>` in the pack declares no `<argument mode="dry-run">`, so it cannot run without writing files. The `<…>` is the generator id.

## Fix

Run the generator without `--dry-run`, or use a generator/pack version that supports dry-run.

## Trigger in the source

```cpp
if (m_dryRun && !generator->IsDryRunCapable(generatorExe)) {
```

## Note

ExecuteGenerator passes the executable path as the host type to IsDryRunCapable, so a dry-run argument restricted with a host attribute is never recognized.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5159-5162`
- `libs/rtemodel/src/RteGenerator.cpp:307-319`
- `tools/projmgr/test/src/ProjMgrGeneratorUnitTests.cpp:151-166`
- `test/packs/ARM/RteTestGenerator/0.1.0/ARM.RteTestGenerator.pdsc:110-130`
