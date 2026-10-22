---
id: "ts-svdconv-m206"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M206: DerivedFrom not found: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M206"
symptoms: ["M206", "DerivedFrom not found: '%NAME%'"]
symptom_regex: "^DerivedFrom not found: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check derivate."
summary: "svdconv resolves a peripheral's derivedFrom attribute against the peripherals already defined in the SVD file."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)"]
---

## Symptom

`M206`
`DerivedFrom not found: '%NAME%'`

## Cause

svdconv resolves a peripheral's derivedFrom attribute against the peripherals already defined in the SVD file. The name in the message is the derivedFrom value that could not be matched to any peripheral name in the SVD, so the referenced base peripheral is missing, misspelled, or defined after the derived one.

## Fix

Check the derivedFrom attribute of the peripheral named in the message. Make sure its value matches the name of an existing peripheral exactly (case-sensitive), and that the base peripheral is defined in the same SVD file. If the base is defined later in the file, move it before the derived peripheral, or give the full definition instead of derivedFrom.

## Note

Source lines were not available, so the cause and fix rely on the message text and the README's brief 'Check derivate' cause. The ordering and case-sensitivity points are my reading of how name lookup usually works, not confirmed from the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)`
