---
id: "ts-csolution-pdsc-file-was-not-found-in"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: pdsc file was not found in: …"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["pdsc file was not found in: <…>"]
symptom_regex: "^pdsc file was not found in: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:1807"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A project-local pack entry (a pack item with a path, in the csolution pack list) points to a directory that exists, but the expected PDSC file is not in it."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1798-1809"]
---

## Symptom

`pdsc file was not found in: <…>`

## Cause

A project-local pack entry (a pack item with a path, in the csolution pack list) points to a directory that exists, but the expected PDSC file is not in it. The tool builds the name as <vendor>.<name>.pdsc from the pack's vendor and name and looks for it inside the path. The message prints the configured path (<…>) of that pack entry.

## Fix

Check the pack entry's path and the pack identity it is given. The directory named by the path must contain a file named <vendor>.<name>.pdsc, where vendor and name match the pack entry (for example Keil.STM32F4xx_DFP.pdsc for vendor Keil and name STM32F4xx_DFP). Rename the PDSC file or correct the vendor/name in the pack entry so they agree, or correct the path to the directory that holds the PDSC.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(pdscFile)) {
```

## Note

The check uses the vendor and name from the pack entry, so a mismatch in those fields produces the same message even when a PDSC file exists in the directory under another name. The message prints packageEntry.path, not the full resolved path, so the user has to match it to the entry in the project file.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1798-1809`
