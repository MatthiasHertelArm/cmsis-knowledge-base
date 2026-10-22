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
summary: "A `$Pack(vendor::name)$` access sequence in a csolution YAML file (for example in a path or file reference) names a pack that matches none of the packs loaded for the context."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3684-3705", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3692-3705", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3702-3704", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3727-3729"]
---

## Symptom

`access sequence pack was not loaded: '$Pack(<…>)$'`

## Cause

A `$Pack(vendor::name)$` access sequence in a csolution YAML file (for example in a path or file reference) names a pack that matches none of the packs loaded for the context. ExpandPackDir scans the loaded packages for one whose vendor and name match the argument; if none matches, the replacement stays empty and the sequence is left unexpanded. The `<…>` in the message is the pack argument as written in the sequence, and the source line 3703 prints it back as `$Pack(<pack>)$`.

## Fix

Check that the pack named inside `$Pack(...)$` is spelled as vendor::name and matches a pack that is installed and listed in the csolution's `packs:` section (or in the project's `packs:` entry), then rebuild. Example: `packs: - pack: Vendor::PackName` with the same vendor and name used in the access sequence.

## Trigger in the source

```cpp
if (replacement.empty()) {
```

## Note

The message is a warning and ExpandPackDir returns without changing the item, so the build continues with the raw sequence text. The README has no entry for this message. The cause is inferred from the matching loop; the pack may be missing from the loaded set for reasons beyond the spelling, such as the pack not being installed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3684-3705`
- `tools/projmgr/src/ProjMgrWorker.cpp:3692-3705`
- `tools/projmgr/src/ProjMgrWorker.cpp:3702-3704`
- `tools/projmgr/src/ProjMgrWorker.cpp:3727-3729`
