---
id: "ts-svdconv-m385"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M385: PMU not supported for CPU '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M385"
symptoms: ["M385", "PMU not supported for CPU '%NAME%'"]
symptom_regex: "^PMU not supported for CPU '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv reports that the PMU (Performance Monitoring Unit) is not supported for the CPU named in the message."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M385`
`PMU not supported for CPU '%NAME%'`

## Cause

svdconv reports that the PMU (Performance Monitoring Unit) is not supported for the CPU named in the message. The %NAME% placeholder is the CPU name from the SVD device's CPU section, which svdconv does not have a PMU mapping for. This is inferred from the message text only; the source lines were not available.

## Fix

Check the <cpu> element of the input SVD file and confirm the CPU name is one svdconv recognises. If the PMU is not needed for your output, remove or leave out the PMU-related setting for that CPU and rerun svdconv. Verify the exact accepted CPU names in the svdconv source or documentation before changing the name.

## Note

Trigger and handling were not checked against the source lines, which were unavailable. The cause and fix are inferred from the message wording and should be verified before relying on them.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
