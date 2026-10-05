---
id: "ts-packchk-m202"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M202: No PDSC input file specified"
status: "draft"
tool: "packchk"
severity: "error"
code: "M202"
symptoms: ["M202", "No PDSC input file specified"]
symptom_regex: "^No PDSC input file specified$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct the command line. **packchk** expects a *.pdsc file name as input."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:86", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:94-110", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackOptions.cpp:171-176", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:208", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:131"]
---

## Symptom

`M202`
`No PDSC input file specified`

## Cause

packchk got no PDSC file to check: no file argument was given, or the argument names a folder instead of a *.pdsc file.

## Fix

Pass the path of the pack's .pdsc file as the positional argument, not the pack folder, e.g. packchk ./MyVendor.MyPack.pdsc.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:86`
- `tools/packchk/src/CreateModel.cpp:94-110`
- `tools/packchk/src/PackOptions.cpp:171-176`
- `tools/packchk/src/ParseOptions.cpp:208`
- `tools/packchk/README.md:131`
