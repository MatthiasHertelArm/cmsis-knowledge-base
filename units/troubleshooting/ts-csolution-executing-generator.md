---
id: "ts-csolution-executing-generator"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: executing generator '…' for context '…' failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["executing generator '<…>' for context '<…>' failed"]
symptom_regex: "^executing generator '.+?' for context '.+?' failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5177"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution runs the generator's command line (built at line 5163) through CrossPlatformUtils::ExecCommand from the generator's working directory."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5163", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5170-5172", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5174", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5176-5178"]
---

## Symptom

`executing generator '<…>' for context '<…>' failed`

## Cause

csolution runs the generator's command line (built at line 5163) through CrossPlatformUtils::ExecCommand from the generator's working directory. The message is printed when that process returns a non-zero exit status, so the generator itself reported a failure. The generator's own output was logged just before at Info level as "generator '<id>' for context '<context>' reported:", and that output holds the actual error. The placeholders are the generator ID and the selected context name.

## Fix

Read the output printed by the preceding "reported:" Info line and fix the problem it describes, such as missing inputs or a bad generator configuration. To reproduce, run the generator's expanded command line by hand from the generator's working directory (the directory csolution changes into before running it) and check its exit code. After fixing the cause, rerun the csolution command.

## Trigger in the source

```cpp
if (result.second) {
```

## Note

The message carries no detail of its own; the useful information is the generator output logged at line 5174. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5163`
- `tools/projmgr/src/ProjMgrWorker.cpp:5170-5172`
- `tools/projmgr/src/ProjMgrWorker.cpp:5174`
- `tools/projmgr/src/ProjMgrWorker.cpp:5176-5178`
