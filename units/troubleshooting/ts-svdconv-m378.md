---
id: "ts-svdconv-m378"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M378: Register Array: Register '…' size (…Bit) does not match <dimIncrement> (…Bit)."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M378"
symptoms: ["M378", "Register Array: Register '%NAME%' size (%NUM%Bit) does not match <dimIncrement> (%NUM2%Bit)."]
symptom_regex: "^Register Array: Register '.+?' size \\(.+?Bit\\) does not match <dimIncrement> \\(.+?Bit\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a register array in the SVD whose register size (the <size> of the register, shown as %NUM% bits) differs from the <dimIncrement> of its <register> array definition (shown as %NUM2% bits)."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M378`
`Register Array: Register '%NAME%' size (%NUM%Bit) does not match <dimIncrement> (%NUM2%Bit).`

## Cause

svdconv found a register array in the SVD whose register size (the <size> of the register, shown as %NUM% bits) differs from the <dimIncrement> of its <register> array definition (shown as %NUM2% bits). In a register array the register size should match the dimension increment so the elements do not overlap or leave gaps that the size does not describe. The named register '%NAME%' is the one where the mismatch was detected.

## Fix

Open the SVD file, find the register named in the message, and make its <size> equal to the <dimIncrement> of its enclosing <dim> array, or correct the <dimIncrement> if it was entered wrongly. Then rerun svdconv on the corrected file.

## Note

The source lines were not available, so the trigger condition and the fix are taken from the message text and the README entry only; the cause is my reading of the message wording, not verified against the code.
