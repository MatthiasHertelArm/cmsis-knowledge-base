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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrWorker.cpp:1807"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `packs:` entry with `path:` points to a folder that exists but does not contain `<Vendor>.<Name>.pdsc` for the pack named in `pack:`; `<…>` is the path."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:1807", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/test_local_pack_file_not_found.csolution.yml:73", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:3919"]
---

## Symptom

`pdsc file was not found in: <…>`

## Cause

A `packs:` entry with `path:` points to a folder that exists but does not contain `<Vendor>.<Name>.pdsc` for the pack named in `pack:`; `<…>` is the path. The file name is built from the `pack:` value, so a vendor or name that differs from the pdsc file name also triggers it.

## Fix

Point `path:` to the folder that holds the pdsc file, and make `pack: <Vendor>::<Name>` match the file `<Vendor>.<Name>.pdsc` there.

## Trigger in the source

```cpp
if (!RteFsUtils::Exists(pdscFile)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:1807`
- `tools/projmgr/test/data/TestSolution/test_local_pack_file_not_found.csolution.yml:73`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:3919`
