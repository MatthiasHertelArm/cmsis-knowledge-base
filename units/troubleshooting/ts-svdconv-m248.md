---
id: "ts-svdconv-m248"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M248: C Expression: Referenced Object must be Register or Field!"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M248"
symptoms: ["M248", "C Expression: Referenced Object must be Register or Field!"]
symptom_regex: "^C Expression: Referenced Object must be Register or Field!$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The message is printed when a C expression in the SVD (for example in a dimIndex, a derived value, or a reference inside the description) refers to a name that resolves to an object that is neither a register …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M248`
`C Expression: Referenced Object must be Register or Field!`

## Cause

The message is printed when a C expression in the SVD (for example in a dimIndex, a derived value, or a reference inside the description) refers to a name that resolves to an object that is neither a register nor a field. The trigger source was not available, so the exact expression site is not confirmed; the message text alone indicates that the referenced symbol is of the wrong kind.

## Fix

Check the SVD expression that the message refers to and make sure the name it references is the name of a register or a field, not a peripheral, cluster or other element. Correct the reference and run svdconv again.

## Note

Trigger lines were not available; the cause and fix are inferred from the message text only. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
