---
id: "ts-svdconv-m355"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M355: No Interrupts found on pos. 0..15. External (Vendor-)Interrupts possibly defined on position 16+. …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M355"
symptoms: ["M355", "No Interrupts found on pos. 0..15. External (Vendor-)Interrupts possibly defined on position 16+. External Interrupts must start on position 0"]
symptom_regex: "^No Interrupts found on pos\\. 0\\.\\.15\\. External \\(Vendor\\-\\)Interrupts possibly defined on position 16\\+\\. External Interrupts must start on position 0$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD describes peripheral interrupts only at positions 16 and above, so no interrupts are found at positions 0 to 15. svdconv treats vendor (external) interrupts as starting at position 0, so the SVD's interrupt numbering does not match …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M355`
`No Interrupts found on pos. 0..15. External (Vendor-)Interrupts possibly defined on position 16+. External Interrupts must start on position 0`

## Cause

The SVD describes peripheral interrupts only at positions 16 and above, so no interrupts are found at positions 0 to 15. svdconv treats vendor (external) interrupts as starting at position 0, so the SVD's interrupt numbering does not match what the tool expects. Only the message text and the README are available here, not the trigger source lines, so this reading of the trigger is an inference.

## Fix

Renumber the interrupt values in the SVD so that external (vendor) interrupts start at position 0, matching the device's interrupt vector numbering, then rerun svdconv. Check the SVD <interrupt> value elements against the device reference manual or vector table.

## Note

Trigger source lines were not provided; the cause is inferred from the message text (no interrupts on positions 0..15, external interrupts expected from position 0). The README's documented cause and fix were not supplied for comparison.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
