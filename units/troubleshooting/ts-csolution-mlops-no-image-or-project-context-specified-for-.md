---
id: "ts-csolution-mlops-no-image-or-project-context-specified-for-"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: mlops: no image or project-context specified for target '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["mlops: no image or project-context specified for target '<…>'"]
symptom_regex: "^mlops: no image or project\\-context specified for target '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrMlops.cpp:201"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution's mlops section names a hardware or simulator target type, but no image entry or project-context matching that target produced a context."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:199-204", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrMlops.cpp:174-176"]
---

## Symptom

`mlops: no image or project-context specified for target '<…>'`

## Cause

The csolution's mlops section names a hardware or simulator target type, but no image entry or project-context matching that target produced a context. CollectSettings builds context names from each target set image's context (or the solution name) plus '+' and the target type, and looks them up among the loaded contexts. When the lookup finds none for a target that was explicitly given, the tool reports the error. The '<…>' in the message is the target type, with '@' and the target set appended when one is given.

## Fix

Check the mlops hardware/simulator target entries in the csolution YAML against the target-types and target-set definitions. Make sure the referenced target type has an image in the target set, or a project-context whose name matches the context the tool builds, and that the target type and target set spellings match. Then re-run csolution.

## Trigger in the source

```cpp
if (!t.targetType.empty() && ref.empty()) {
```

## Note

The README does not document this message. The cause is inferred from the context-name lookup in the source; the exact user-facing YAML layout that makes the match succeed is not shown in the lines given.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrMlops.cpp:199-204`
- `tools/projmgr/src/ProjMgrMlops.cpp:174-176`
