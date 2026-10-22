---
id: "ts-csolution-was-not-found-2"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: generator '…' was not found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["generator '<…>' was not found"]
symptom_regex: "^generator '.+?' was not found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5113"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ExecuteGenerator processes the selected context and then looks up the requested generator id in context.generators."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5111-5115", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5108-5110"]
---

## Symptom

`generator '<…>' was not found`

## Cause

ExecuteGenerator processes the selected context and then looks up the requested generator id in context.generators. The message is printed when that id is not among the generators the context resolved, so the id given to the run does not match any generator declared for the project's components, gpdsc files, or selected context.

## Fix

Use a generator id exactly as the pack declares it, and make sure the pack providing that generator is part of the project and the selected context. Check the spelling and case of the id against the generator entries in the pack's PDSC and in the project's gpdsc or component files. Then run again with the corrected id.

## Trigger in the source

```cpp
if (generators.find(generatorId) == generators.end()) {
```

## Note

The lines do not show how generatorId is supplied to ExecuteGenerator, so the exact command-line option is not named here. The lookup relies on context.generators being filled by ProcessContext, which is not in the lines given. Other messages in this function, such as 'generator executable ... was not found', use the same wording but are triggered by a different check.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5111-5115`
- `tools/projmgr/src/ProjMgrWorker.cpp:5108-5110`
