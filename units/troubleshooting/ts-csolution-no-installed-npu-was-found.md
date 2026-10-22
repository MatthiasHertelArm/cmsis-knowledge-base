---
id: "ts-csolution-no-installed-npu-was-found"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: no installed NPU was found"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["no installed NPU was found"]
symptom_regex: "^no installed NPU was found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4386"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution `list npus` path (ListNpus) collects NPU information from the selected contexts after loading packs and applying the target attributes."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4355-4388", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4370-4371", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4385-4386"]
---

## Symptom

`no installed NPU was found`

## Cause

The csolution `list npus` path (ListNpus) collects NPU information from the selected contexts after loading packs and applying the target attributes. If no context yields any NPU entry, the map of NPU info is empty and the tool reports that no installed NPU was found. The source lines show only the empty check and the collection loop; they do not show which packs or NPU entries the user lacks.

## Fix

Check that the packs providing NPU (Ethos-U) support are installed for the selected context, for example by running `cpackget list` or checking the CMSIS pack cache, and then run the list command again. The source gives no specific command, so treat this as a suggestion to verify the installation.

## Trigger in the source

```cpp
if (npuInfos.empty()) {
```

## Note

The message is not documented in the README. The message text says 'installed NPU', but the code only checks whether any NPU info was collected from the contexts, so the cause could also be a target or filter that matches no NPU. The filtered variant ('no NPU was found with filter') is a separate message printed at line 4436.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4355-4388`
- `tools/projmgr/src/ProjMgrWorker.cpp:4370-4371`
- `tools/projmgr/src/ProjMgrWorker.cpp:4385-4386`
