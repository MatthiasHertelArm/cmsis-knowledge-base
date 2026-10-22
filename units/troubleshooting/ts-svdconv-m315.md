---
id: "ts-svdconv-m315"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M315: Address Block: <size> is zero."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M315"
symptoms: ["M315", "Address Block: <size> is zero."]
symptom_regex: "^Address Block: <size> is zero\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file has an <addressBlock> element whose <size> child is zero. svdconv reports the zero size as an error for that address block, because an address block must cover at least one byte of the peripheral's register space."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)"]
---

## Symptom

`M315`
`Address Block: <size> is zero.`

## Cause

The SVD file has an <addressBlock> element whose <size> child is zero. svdconv reports the zero size as an error for that address block, because an address block must cover at least one byte of the peripheral's register space. The message text names the address block and the <size> value that is zero.

## Fix

Open the SVD file, find the <addressBlock> that the message refers to, and set its <size> to the byte length of the register region it covers (for example 0x400 for a 1 KB block). Then run svdconv again. If the peripheral really has no address block, remove that <addressBlock> element rather than leaving size at zero.

## Note

Cause and fix are inferred from the message text and the README entry for M315; the source lines around the trigger were not available to confirm the exact check.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)`
