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
summary: "Filenames are case sensitive."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:124-126", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:511-570", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:159"]
---

## Symptom

`M310`
`Filename mismatch (case sensitive):   PDSC name : '%PDSC%'   Filename  : '%SYSTEM%'`

## Cause

Filenames are case sensitive. Correct spelling.

## Fix

Change the path in the PDSC so every folder and file name has exactly the letter case used on disk, or rename the files; 'Filename' in the message shows the on-disk spelling.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:124-126`
- `tools/packchk/src/CheckFiles.cpp:511-570`
- `tools/packchk/README.md:159`
