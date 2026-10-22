---
id: "ts-svdconv-m391"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M391: CPU: configured number of SAU regions '…' greater than <sauNumRegions> value: '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M391"
symptoms: ["M391", "CPU: configured number of SAU regions '%NUM%' greater than <sauNumRegions> value: '%NUM2%'"]
symptom_regex: "^CPU: configured number of SAU regions '.+?' greater than <sauNumRegions> value: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The CPU section of the SVD input configures a number of SAU (Security Attribution Unit) regions that is larger than the value of the sauNumRegions element it declares for the CPU."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M391 text; trigger not available in the clone)"]
---

## Symptom

`M391`
`CPU: configured number of SAU regions '%NUM%' greater than <sauNumRegions> value: '%NUM2%'`

## Cause

The CPU section of the SVD input configures a number of SAU (Security Attribution Unit) regions that is larger than the value of the sauNumRegions element it declares for the CPU. The first %NUM% is the configured region count and the second %NUM2% is the sauNumRegions value that svdconv read. The mismatch means the device description is internally inconsistent about how many SAU regions exist.

## Fix

Check the CPU element of the SVD file: make the sauNumRegions value match the number of SAU regions the device actually has, or reduce the configured SAU region count so it does not exceed sauNumRegions. Then rerun svdconv.

## Note

Source lines were not available, so the trigger condition and the exact element that holds the configured count are inferred from the message text only. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message M391 text; trigger not available in the clone)`
