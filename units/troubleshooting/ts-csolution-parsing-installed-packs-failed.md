---
id: "ts-csolution-parsing-installed-packs-failed"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: parsing installed packs failed"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["parsing installed packs failed"]
symptom_regex: "^parsing installed packs failed$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:570"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "csolution reaches this error when it loads the installed packs for the selected contexts and the RTE kernel fails to return the effective PDSC file list (GetEffectivePdscFiles returns false)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:514", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:566-573"]
---

## Symptom

`parsing installed packs failed`

## Cause

csolution reaches this error when it loads the installed packs for the selected contexts and the RTE kernel fails to return the effective PDSC file list (GetEffectivePdscFiles returns false). The check runs only when the solution has no explicit pack requirements, or the load-packs policy is ALL or LATEST (or DEFAULT, which maps to latest). The kernel is pointed at the CMSIS pack root set at line 514, so the failure concerns the installed pack store that root points to. The source lines shown do not include GetEffectivePdscFiles, so the specific reason for its failure is not visible here.

## Fix

Read the error and warning lines printed just before this one, since the kernel usually logs the underlying problem (for example an unreadable or malformed installed pack description) before returning false. Check that the CMSIS pack root the build uses holds a valid pack installation, and repair or reinstall any packs the earlier messages name. If the solution does not need installed packs, declare the required packs explicitly in the csolution YAML so this path is skipped.

## Trigger in the source

```cpp
if (!m_kernel->GetEffectivePdscFiles(pdscFiles, latest)) {
```

## Note

The message has no code and is not documented in the README. The underlying kernel failure reason is not in the lines given, so the cause is inferred from the trigger and its condition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:514`
- `tools/projmgr/src/ProjMgrWorker.cpp:566-573`
