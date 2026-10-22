---
id: "ts-packchk-m310"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M310: Filename mismatch (case sensitive): PDSC name : '…' Filename : '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M310"
symptoms: ["M310", "Filename mismatch (case sensitive):   PDSC name : '%PDSC%'   Filename  : '%SYSTEM%'"]
symptom_regex: "^Filename mismatch \\(case sensitive\\):   PDSC name : '.+?'   Filename  : '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Filenames are case sensitive. Correct spelling."
summary: "packchk compares the file name written in the PDSC against the name of the file on disk, and the two differ in letter case."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the clone; the message text and README cause were used)"]
---

## Symptom

`M310`
`Filename mismatch (case sensitive):   PDSC name : '%PDSC%'   Filename  : '%SYSTEM%'`

## Cause

packchk compares the file name written in the PDSC against the name of the file on disk, and the two differ in letter case. Filenames are matched case sensitively, so a PDSC that refers to a file as, for example, 'Device.H' while the file is named 'device.h' triggers this message. The %PDSC% placeholder is the name the PDSC uses and %SYSTEM% is the name found on the file system.

## Fix

Make the file name in the PDSC match the file on disk exactly, including upper and lower case. Rename either the file or the PDSC entry so both use the same spelling, then rerun packchk.

## Note

The source lines were not available, so the trigger and the exact comparison were not verified; the cause is inferred from the message text and the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (trigger not available in the clone; the message text and README cause were used)`
