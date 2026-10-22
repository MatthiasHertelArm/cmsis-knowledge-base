---
id: "ts-svdconv-m344"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M344: Register '…' (@…) is outside or does not fit any <addressBlock> specified for Peripheral '…' …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M344"
symptoms: ["M344", "Register '%NAME%' (@%ADDRSIZE%) is outside or does not fit any <addressBlock> specified for Peripheral '%NAME2%' %TEXT%"]
symptom_regex: "^Register '.+?' \\(@.+?\\) is outside or does not fit any <addressBlock> specified for Peripheral '.+?' .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv checks each register of a peripheral against the address blocks declared for that peripheral in the SVD file."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M344`
`Register '%NAME%' (@%ADDRSIZE%) is outside or does not fit any <addressBlock> specified for Peripheral '%NAME2%' %TEXT%`

## Cause

svdconv checks each register of a peripheral against the address blocks declared for that peripheral in the SVD file. The warning means a register's address offset places it outside every <addressBlock> of the named peripheral, or the register extends past the end of the block that contains its start. The %NAME% and %ADDRSIZE% values identify the register and its address; %NAME2% names the peripheral. The source was not available, so this is inferred from the message text alone.

## Fix

Open the SVD file, find the peripheral named in the message, and compare the <offset> and <size> of the register with the <offset> and <size> of its <addressBlock>. Either enlarge the address block so it covers the register, or correct the register's <addressOffset> if it was mistyped. Then rerun svdconv.

## Note

Source lines were not available for this entry, so the trigger condition and the handling are inferred from the message wording and not confirmed in code. Treat the cause as a reading of the message text. The README is documented as covering this message, but its text was not provided for comparison.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
