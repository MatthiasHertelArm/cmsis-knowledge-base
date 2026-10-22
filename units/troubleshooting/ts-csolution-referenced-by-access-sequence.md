---
id: "ts-csolution-referenced-by-access-sequence"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: context '…' referenced by access sequence '…' is not compatible"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["context '<…>' referenced by access sequence '<…>' is not compatible"]
symptom_regex: "^context '.+?' referenced by access sequence '.+?' is not compatible$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3746"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The access sequence in a solution-level csolution file references a context (for example '$Source(<name>)$' style sequence with a context argument) by a name fragment, and no context in the loaded set contains that fragment as a substring."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3737-3747", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3739-3744"]
---

## Symptom

`context '<…>' referenced by access sequence '<…>' is not compatible`

## Cause

The access sequence in a solution-level csolution file references a context (for example '$Source(<name>)$' style sequence with a context argument) by a name fragment, and no context in the loaded set contains that fragment as a substring. Solution-level processing requires the referenced context name to match a known compatible context, so the lookup finds nothing and the tool stops. The '<…>' context value is the referenced name from the access sequence, and the sequence name is the access sequence being expanded.

## Fix

Check the access sequence in the solution's csolution.yml or the project file that names the context, and correct the context name so it matches a context that the solution actually defines (for example a project and build-type/target combination such as project+target). Make sure that context is part of the solution and compatible with its target and type settings, then run the build again.

## Trigger in the source

```cpp
if (compatibleContexts.empty()) {
```

## Note

The README does not document this message. The cause is inferred from the substring match over m_contexts at solution level; the exact syntax of the access sequence with a context argument is not shown in the lines given, so the fix describes checking the name rather than a specific option.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3737-3747`
- `tools/projmgr/src/ProjMgrWorker.cpp:3739-3744`
