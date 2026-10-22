---
id: "ts-svdconv-m388"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M388: MVE Floating-Point support is set but MVE is not set"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M388"
symptoms: ["M388", "MVE Floating-Point support is set but MVE is not set"]
symptom_regex: "^MVE Floating\\-Point support is set but MVE is not set$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD device or peripheral description sets MVE floating-point support (the MVE FP feature) while MVE itself is not enabled for the same core."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)"]
---

## Symptom

`M388`
`MVE Floating-Point support is set but MVE is not set`

## Cause

The SVD device or peripheral description sets MVE floating-point support (the MVE FP feature) while MVE itself is not enabled for the same core. MVE floating-point requires the MVE extension, so the combination is rejected. The exact element names are not available in the lines given, so this reading is inferred from the message text.

## Fix

Enable the MVE (Helium) feature in the SVD core description alongside the MVE floating-point setting, or remove the MVE floating-point setting if the target core has no MVE. Then rerun svdconv on the SVD file.

## Note

Source lines were not available, so the trigger and the exact SVD elements involved were not verified; the cause is inferred from the message wording. README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the given lines; message text only)`
