---
id: "ts-svdconv-m329"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M329: CPU Type is not set, using default (Cortex-M3)"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M329"
symptoms: ["M329", "CPU Type is not set, using default (Cortex-M3)"]
symptom_regex: "^CPU Type is not set, using default \\(Cortex\\-M3\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file being converted has no CPU element (or its CPU Type is empty), so svdconv cannot determine the target core and falls back to its default of Cortex-M3."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M329`
`CPU Type is not set, using default (Cortex-M3)`

## Cause

The SVD file being converted has no CPU element (or its CPU Type is empty), so svdconv cannot determine the target core and falls back to its default of Cortex-M3. The message is a warning about that fallback, and the generated output may not match the actual device core.

## Fix

Add a complete <cpu> block to the SVD file under <device>, naming the real core in <name> (for example CM4 or CM7) together with the required <revision>, <endian>, <mpuPresent>, <fpuPresent> and <nvicPrioBits> elements, or correct the existing <name> value. Then rerun svdconv.

## Note

Only the message text and the README are known here; the source lines were not available, so the trigger condition and the default behaviour are inferred from the message rather than read from code. The message is labelled severity error in the catalog but its text reads as a fallback notice, which a reviewer should check against the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
