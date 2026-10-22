---
id: "ts-svdconv-m350"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M350: Peripheral '…' (@…) is not 4Byte-aligned."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M350"
symptoms: ["M350", "Peripheral '%NAME%' (@%ADDR%) is not 4Byte-aligned."]
symptom_regex: "^Peripheral '.+?' \\(@.+?\\) is not 4Byte\\-aligned\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv checks each peripheral's base address and prints this warning when the address is not a multiple of 4 bytes, so the peripheral does not start on a 32-bit word boundary. %NAME% is the peripheral name from the SVD …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M350`
`Peripheral '%NAME%' (@%ADDR%) is not 4Byte-aligned.`

## Cause

svdconv checks each peripheral's base address and prints this warning when the address is not a multiple of 4 bytes, so the peripheral does not start on a 32-bit word boundary. %NAME% is the peripheral name from the SVD file and %ADDR% is its baseAddress. The check is inferred from the message text only, since the source lines were not available.

## Fix

Open the SVD file, find the peripheral named in the message, and correct its baseAddress so that it is a multiple of 4 (last hex digit 0, 4, 8 or C). If the address is correct and the warning is expected, it can be left as is, since it does not stop the conversion.

## Note

Source lines were not available, so the trigger condition and the severity handling are not confirmed from code; the cause is read from the message text and the README entry is assumed to match it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
