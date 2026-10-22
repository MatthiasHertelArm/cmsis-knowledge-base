---
id: "ts-svdconv-m105"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M105: Cannot add Register to group sorter: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M105"
symptoms: ["M105", "Cannot add Register to group sorter: '%NAME%'"]
symptom_regex: "^Cannot add Register to group sorter: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv could not add a register named in the message to its internal register group, which happens while it processes the SVD peripheral and register definitions."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M105`
`Cannot add Register to group sorter: '%NAME%'`

## Cause

svdconv could not add a register named in the message to its internal register group, which happens while it processes the SVD peripheral and register definitions. The source lines were not available, so the exact trigger condition is not confirmed; the variable part %NAME% is the register name the tool was handling when the insertion failed.

## Fix

Check the SVD file for the register named in the message: make sure its name is unique within its peripheral and that its address offset and size are valid and not duplicated or overlapping with another register in the same group. Correct the SVD entry and re-run svdconv.

## Note

Source lines were unavailable, so the cause and fix are inferred from the message text alone and should be verified against the source before relying on them. The README is documented as having a cause and fix for this message, but its text was not provided to confirm.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
