---
id: "ts-svdconv-m389"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M389: Specified <deviceNumInterrupts>: '…' greater or equal '…': '…'."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M389"
symptoms: ["M389", "Specified <deviceNumInterrupts>: '%NUM%' greater or equal '%NAME%': '%NUM2%'."]
symptom_regex: "^Specified <deviceNumInterrupts>: '.+?' greater or equal '.+?': '.+?'\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv compares the device's declared interrupt count (deviceNumInterrupts) against the number of interrupts actually listed in the SVD, and prints this error when the declared count is greater than or equal to the bound it checks against (the %NAME%/%NUM2% pair)."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M389`
`Specified <deviceNumInterrupts>: '%NUM%' greater or equal '%NAME%': '%NUM2%'.`

## Cause

svdconv compares the device's declared interrupt count (deviceNumInterrupts) against the number of interrupts actually listed in the SVD, and prints this error when the declared count is greater than or equal to the bound it checks against (the %NAME%/%NUM2% pair). The SVD's <deviceNumInterrupts> value does not agree with the interrupt definitions in the file.

## Fix

Open the SVD and correct the <deviceNumInterrupts> value so it matches the interrupt entries the device actually defines, or remove the element if it is not needed, then rerun svdconv. Source lines were not available to confirm which bound the check uses.

## Note

Derived from the message text only; the clone was not available, so the exact comparison bound and the README entry (not documented) are unverified.
