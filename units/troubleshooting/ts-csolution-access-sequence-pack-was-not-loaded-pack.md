---
id: "ts-csolution-access-sequence-pack-was-not-loaded-pack"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: access sequence pack was not loaded: '$Pack(…)$'"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["access sequence pack was not loaded: '$Pack(<…>)$'"]
symptom_regex: "^access sequence pack was not loaded: '\\$Pack\\(.+?\\)\\$'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3703"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `$Pack(vendor::name)$` access sequence in a csolution input (for example a path in a component or build setting) names a pack that no loaded pack matches."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3684-3690", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3691-3705", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3727-3729"]
---

## Symptom

`access sequence pack was not loaded: '$Pack(<…>)$'`

## Cause

A `$Pack(vendor::name)$` access sequence in a csolution input (for example a path in a component or build setting) names a pack that no loaded pack matches. ExpandPackDir walks the loaded packs and compares each pack ID with the requested vendor and name; if none matches, the replacement stays empty. The `<…>` in the message is the pack reference as written, and the message repeats it wrapped in `$Pack(...)$`. The pack is probably not installed in the pack root, not listed in the required packs, or spelled differently from the installed pack.

## Fix

Check the `$Pack(...)$` argument against the pack that is actually installed, using the vendor::name form. Make sure the pack is declared under the project's packs or the solution's required packs, and install it with cpackget or the pack manager if it is missing. Then rerun the build. The source gives no other way to resolve it.

## Trigger in the source

```cpp
if (replacement.empty()) {
```

## Note

The warning is emitted through ProjMgrLogger::Warn and processing continues without replacing the sequence, so the item keeps its unexpanded $Pack(...)$ text. The cause is inferred from the matching loop; the source does not say which pack set is searched for the missing pack. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3684-3690`
- `tools/projmgr/src/ProjMgrWorker.cpp:3691-3705`
- `tools/projmgr/src/ProjMgrWorker.cpp:3727-3729`
