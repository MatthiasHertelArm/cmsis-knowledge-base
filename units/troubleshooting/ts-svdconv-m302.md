---
id: "ts-svdconv-m302"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M302: Size of Register '…:…' must be 8, 16 or 32 Bits"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M302"
symptoms: ["M302", "Size of Register '%NAME%:%NUM%' must be 8, 16 or 32 Bits"]
symptom_regex: "^Size of Register '.+?:.+?' must be 8, 16 or 32 Bits$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv warns when a register in the SVD file has a <size> value other than 8, 16 or 32 bits."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)"]
---

## Symptom

`M302`
`Size of Register '%NAME%:%NUM%' must be 8, 16 or 32 Bits`

## Cause

svdconv warns when a register in the SVD file has a <size> value other than 8, 16 or 32 bits. The %NAME% and %NUM% placeholders are the register name and its index in the SVD, so the warning points at the offending register. Only those three widths are accepted for register access, so a register declared with e.g. 64 or 12 bits (or a size inherited from a peripheral or cluster that resolves to another value) triggers it.

## Fix

Open the SVD and find the register named in the message. Correct its <size> element (or the <size> inherited from its parent <peripherals>/<registers> default) to 8, 16 or 32, matching the real access width of the hardware register. Then re-run svdconv.

## Note

Source lines were not available, so the trigger condition is inferred from the message text and README; verify against SVDConv_Msgs.cpp before relying on the exact wording of the cause.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)`
