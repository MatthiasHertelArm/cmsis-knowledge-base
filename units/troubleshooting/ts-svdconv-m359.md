---
id: "ts-svdconv-m359"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M359: Address Block: <usage> not set."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M359"
symptoms: ["M359", "Address Block: <usage> not set."]
symptom_regex: "^Address Block: <usage> not set\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file has an <addressBlock> element in a peripheral or register description that does not contain a <usage> child element, so svdconv cannot tell what the address block is for."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M359`
`Address Block: <usage> not set.`

## Cause

The SVD file has an <addressBlock> element in a peripheral or register description that does not contain a <usage> child element, so svdconv cannot tell what the address block is for. The <usage> value in the message is the address block's usage field such as registers, buffer or reserved.

## Fix

Open the SVD file, find the <addressBlock> element named in the message, and add a <usage> child with a valid value such as registers, buffer or reserved, placed after <offset> and <size> as the CMSIS-SVD schema requires. Then rerun svdconv.

## Note

The source lines were not available, so the trigger is inferred from the message text and the README entry only; verify the exact condition in SVDConv_Msgs.cpp before relying on the evidence path.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
