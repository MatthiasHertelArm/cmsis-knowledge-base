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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5160"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution command was run with the dry-run option, and the selected generator's IsDryRunCapable check returned false for its executable."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5159-5162", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5101-5108"]
---

## Symptom

`generator '<…>' is not dry-run capable`

## Cause

The csolution command was run with the dry-run option, and the selected generator's IsDryRunCapable check returned false for its executable. The generator is identified by the <…> id in the message, and the check only passes when the generator declares dry-run support, so a generator without that support cannot be run in dry-run mode.

## Fix

Run the generator without the dry-run option so it executes normally, or use a generator that declares dry-run capability. The source does not show how a generator declares that capability, so check the generator's own documentation or its package definition for dry-run support.

## Trigger in the source

```cpp
if (m_dryRun && !generator->IsDryRunCapable(generatorExe)) {
```

## Note

The message is printed only when m_dryRun is set and the generator reports it is not dry-run capable. The README does not document this message. The cause is inferred from the trigger; how IsDryRunCapable decides is not in the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5159-5162`
- `tools/projmgr/src/ProjMgrWorker.cpp:5101-5108`
