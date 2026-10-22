---
id: "ts-svdconv-m387"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M387: CPU: <sauNumRegions> set to 0 but regions are configured."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M387"
symptoms: ["M387", "CPU: <sauNumRegions> set to 0 but regions are configured."]
symptom_regex: "^CPU: <sauNumRegions> set to 0 but regions are configured\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD describes the Cortex-M security attribution unit (SAU) with sauNumRegions set to 0, yet the device also lists SAU regions in the CPU section."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; source lines not available in this session)"]
---

## Symptom

`M387`
`CPU: <sauNumRegions> set to 0 but regions are configured.`

## Cause

The SVD describes the Cortex-M security attribution unit (SAU) with sauNumRegions set to 0, yet the device also lists SAU regions in the CPU section. The SVD CPU element is internally inconsistent: a zero region count contradicts the configured regions, so svdconv reports M387 instead of generating the SAU setup.

## Fix

Open the SVD file and check the CPU element. Either set sauNumRegions to the number of SAU regions the device actually has (greater than 0) when regions are described, or remove the SAU region definitions if the core has no SAU. Then rerun svdconv on the corrected file.

## Note

Source lines were not available, so the trigger condition and the exact wording of the SVD fields are inferred from the message text alone. Verify the condition against SVDConv_Msgs.cpp before relying on the fix.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; source lines not available in this session)`
