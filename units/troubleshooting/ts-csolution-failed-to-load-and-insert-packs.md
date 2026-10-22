---
id: "ts-csolution-failed-to-load-and-insert-packs"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: failed to load and insert packs"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["failed to load and insert packs"]
symptom_regex: "^failed to load and insert packs$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:575"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "This message is a wrapper printed when the pack kernel fails to load the collected PDSC files."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:574-577", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:569-572", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:610-613"]
---

## Symptom

`failed to load and insert packs`

## Cause

This message is a wrapper printed when the pack kernel fails to load the collected PDSC files. LoadAllRelevantPacks gathers the PDSC files from the selected contexts and from installed packs (via GetEffectivePdscFiles), then calls LoadAndInsertPacks. The kernel's own error for the specific pack or PDSC that failed, such as a malformed or unreadable PDSC or a pack that cannot be parsed, is logged before this line and is not repeated here. Because LoadPacks defers the return on this failure, the build still continues to the context checks before exiting.

## Fix

Read the error lines printed just before this one, which name the PDSC file or pack that failed to load, and fix that pack. Typically this means repairing or reinstalling the named pack so its .pdsc file is well-formed, and checking that the pack is installed in the pack root the build uses. Then rerun the csolution command.

## Trigger in the source

```cpp
if (!m_kernel->LoadAndInsertPacks(m_loadedPacks, pdscFiles)) {
```

## Note

The message carries no variable part, so it cannot identify the failing pack by itself; the specific cause is only in the kernel's earlier output. CheckRteErrors() decides the return value, so the build may not stop at this line. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:574-577`
- `tools/projmgr/src/ProjMgrWorker.cpp:569-572`
- `tools/projmgr/src/ProjMgrWorker.cpp:610-613`
