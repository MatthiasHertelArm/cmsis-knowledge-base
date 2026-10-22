---
id: "ts-csolution-gpdsc-validation-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: context '…' generator '…' from component '…': gpdsc validation failed"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["context '<…>' generator '<…>' from component '<…>': gpdsc validation failed"]
symptom_regex: "^context '.+?' generator '.+?' from component '.+?': gpdsc validation failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:2901"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The generator's gpdsc file was read successfully, but ProjMgrUtils::ReadGpdscFile reported it as not valid (validGpdsc is false)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2891-2892", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2900-2902", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:2894-2898"]
---

## Symptom

`context '<…>' generator '<…>' from component '<…>': gpdsc validation failed`

## Cause

The generator's gpdsc file was read successfully, but ProjMgrUtils::ReadGpdscFile reported it as not valid (validGpdsc is false). The message names the context, the generator and the component that declared the gpdsc. The source lines shown do not include ReadGpdscFile, so the kind of validation failure is not visible here. Processing continues after this warning, unlike the 'reading gpdsc failed' error, which returns false.

## Fix

Find the validation details that csolution printed for this gpdsc file, which come from ReadGpdscFile and are not shown in the lines given. Correct the reported problems in the gpdsc file, for example by regenerating it with the generator named in the message, then rebuild. If the gpdsc is not fixed, the components it provides are still added to the context, so check that the generated output is what you expect.

## Trigger in the source

```cpp
if (!validGpdsc) {
```

## Note

The README does not document this message. The validation error details are produced inside ProjMgrUtils::ReadGpdscFile, which is outside the lines given, so the specific failure is unknown. The warning does not stop processing, and the gpdsc pack is still attached at line 2904.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:2891-2892`
- `tools/projmgr/src/ProjMgrWorker.cpp:2900-2902`
- `tools/projmgr/src/ProjMgrWorker.cpp:2894-2898`
