---
id: "ts-svdconv-m333"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M333: Duplicate <enumeratedValue> …: '…' (…), already used by '…' (…) …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M333"
symptoms: ["M333", "Duplicate <enumeratedValue> %NUM%: '%NAME%' (%USAGE%), already used by '%NAME2%' (%USAGE2%) %LINE%"]
symptom_regex: "^Duplicate <enumeratedValue> .+?: '.+?' \\(.+?\\), already used by '.+?' \\(.+?\\) .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found two <enumeratedValue> entries inside the same enumeration of the SVD that share the same value (%NUM%) or the same name, so one of them is a duplicate of the other."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M333`
`Duplicate <enumeratedValue> %NUM%: '%NAME%' (%USAGE%), already used by '%NAME2%' (%USAGE2%) %LINE%`

## Cause

svdconv found two <enumeratedValue> entries inside the same enumeration of the SVD that share the same value (%NUM%) or the same name, so one of them is a duplicate of the other. The message names the duplicate (%NAME%, with its usage) and the entry that already uses that value or name (%NAME2%, %USAGE2%), and %LINE% gives the position in the SVD file.

## Fix

Open the SVD file at the reported line and make the enumerated values of that enumeration unique: give each <enumeratedValue> a distinct <value> and a distinct <name>, or remove the entry that is not needed. Then run svdconv again.

## Note

The clone was not available, so the trigger and handling could not be checked in the source; the cause and fix rest on the message text and the README statement that it is documented. The message is a warning, so the conversion may still complete.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
