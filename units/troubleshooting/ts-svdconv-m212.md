---
id: "ts-svdconv-m212"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M212: Address Block <usage> parse error: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M212"
symptoms: ["M212", "Address Block <usage> parse error: '%NAME%'"]
symptom_regex: "^Address Block <usage> parse error: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct address block."
summary: "svdconv prints this when it cannot parse an <addressBlock> element of the SVD file: the address block has a missing or malformed child such as offset, size or usage, or a value that does not parse as a number."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M212`
`Address Block <usage> parse error: '%NAME%'`

## Cause

svdconv prints this when it cannot parse an <addressBlock> element of the SVD file: the address block has a missing or malformed child such as offset, size or usage, or a value that does not parse as a number. The quoted name is the register or peripheral context in which the address block was found.

## Fix

Open the SVD file at the peripheral named in the message and check its <addressBlock> element. Make sure it contains <offset>, <size> and <usage> with valid values (numeric offset and size, usage set to one of the allowed keywords such as registers, buffer or reserved), then run svdconv again.

## Note

The source lines were not available, so the cause is inferred from the message text and the README; the README cause 'Correct address block.' is terse and was not verified against the trigger. The exact validity rules for usage values are not confirmed here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
