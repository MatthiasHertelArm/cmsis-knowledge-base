---
id: "ts-svdconv-m214"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M214: Peripheral '…' <dim> single-instantiation is not supported (use Array instead)."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M214"
symptoms: ["M214", "Peripheral '%NAME%' <dim> single-instantiation is not supported (use Array instead)."]
symptom_regex: "^Peripheral '.+?' <dim> single\\-instantiation is not supported \\(use Array instead\\)\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct Regs to Reg[s]."
summary: "The SVD file describes a peripheral with a dim element that is set up as a single instance rather than as an array, which svdconv does not accept."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M214`
`Peripheral '%NAME%' <dim> single-instantiation is not supported (use Array instead).`

## Cause

The SVD file describes a peripheral with a dim element that is set up as a single instance rather than as an array, which svdconv does not accept. The peripheral name in the message is the one taken from the SVD input.

## Fix

Edit the SVD so the peripheral is written as an array: use a dim element with a dimIncrement and a dim count (for example a count greater than one) with a %s placeholder in the name, or remove the dim element if a single instance is intended, then rerun svdconv.

## Note

The source lines were not available, so the trigger condition and the exact wording of the fix are inferred from the message text alone. The README cause text 'Correct Regs to Reg[s].' is unrelated to this message and appears to be a copy error.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
