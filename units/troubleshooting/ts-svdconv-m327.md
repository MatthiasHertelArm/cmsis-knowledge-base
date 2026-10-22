---
id: "ts-svdconv-m327"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M327: NVIC Prio Bits not set or wrong value, must be 2..8. Using default (4)"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M327"
symptoms: ["M327", "NVIC Prio Bits not set or wrong value, must be 2..8. Using default (4)"]
symptom_regex: "^NVIC Prio Bits not set or wrong value, must be 2\\.\\.8\\. Using default \\(4\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD device description has a cpu/nvicPrioBits element that is missing or holds a value outside the accepted range of 2 to 8, so svdconv cannot use it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; trigger lines not available)"]
---

## Symptom

`M327`
`NVIC Prio Bits not set or wrong value, must be 2..8. Using default (4)`

## Cause

The SVD device description has a cpu/nvicPrioBits element that is missing or holds a value outside the accepted range of 2 to 8, so svdconv cannot use it. The message says it falls back to the default of 4 priority bits. The exact trigger was not visible in the provided lines, so this reading rests on the message text alone.

## Fix

Check the SVD file's <cpu> section and set <nvicPrioBits> to the number of implemented NVIC priority bits for the device, a value between 2 and 8 (for example 4 for a Cortex-M4 with 4 priority bits). Re-run svdconv afterwards to confirm the warning no longer appears.

## Note

Source lines were not available, so the trigger condition and the exact element name are inferred from the message wording and not confirmed in code. Whether the message is an error or a warning in practice should be checked against the severity the tool prints.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; trigger lines not available)`
