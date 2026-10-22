---
id: "ts-csolution-required-packs-must-be-specified"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: required packs must be specified"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["required packs must be specified"]
symptom_regex: "^required packs must be specified$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:563"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The load-packs policy is set to REQUIRED, but none of the selected contexts declares any pack requirements."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:543", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:546", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:562-565", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:567-568"]
---

## Symptom

`required packs must be specified`

## Cause

The load-packs policy is set to REQUIRED, but none of the selected contexts declares any pack requirements. LoadAllRelevantPacks() sets noPackRequirements to true only when every context's packRequirements list is empty, and in that case it refuses to continue, because with the REQUIRED policy the tool loads only the packs the project asks for. The project therefore has no pack entries to load.

## Fix

Add the packs the project needs to the csolution project or context definition so that packRequirements is not empty, then rerun the build. If you do not need the REQUIRED policy, change the load-packs setting to a different policy (ALL, LATEST or DEFAULT are handled in the same function) so the tool loads the installed packs instead.

## Trigger in the source

```cpp
if (noPackRequirements && (m_loadPacksPolicy == LoadPacksPolicy::REQUIRED)) {
```

## Note

The README does not document this message. The source does not show where the REQUIRED policy is set (command line or configuration), so the fix names only the project-side change and the policy alternatives visible in this function. The message has no code and is printed only at this line in the given lines.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:543`
- `tools/projmgr/src/ProjMgrWorker.cpp:546`
- `tools/projmgr/src/ProjMgrWorker.cpp:562-565`
- `tools/projmgr/src/ProjMgrWorker.cpp:567-568`
