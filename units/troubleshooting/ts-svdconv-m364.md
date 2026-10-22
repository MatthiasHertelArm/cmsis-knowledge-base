---
id: "ts-svdconv-m364"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M364: CPU: <sauNumRegions> value '…' greater than SAU max num (…)"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M364"
symptoms: ["M364", "CPU: <sauNumRegions> value '%NUM%' greater than SAU max num (%NUM2%)"]
symptom_regex: "^CPU: <sauNumRegions> value '.+?' greater than SAU max num \\(.+?\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD device description sets the CPU's sauNumRegions element to a value larger than the maximum number of Security Attribution Unit regions that the CPU type supports. svdconv checks the declared count against the per-CPU limit and reports the …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M364`
`CPU: <sauNumRegions> value '%NUM%' greater than SAU max num (%NUM2%)`

## Cause

The SVD device description sets the CPU's sauNumRegions element to a value larger than the maximum number of Security Attribution Unit regions that the CPU type supports. svdconv checks the declared count against the per-CPU limit and reports the declared value and that limit.

## Fix

Open the SVD file, find the <sauNumRegions> element under <cpu>, and correct it to a value no greater than the SAU maximum for the CPU core named in <name>. If the core really has that many regions, check the CPU element against the device reference manual.

## Note

The source lines were not available, so the trigger and the limit check are inferred from the message text alone and the README is not checked; verify against the source before relying on the exact condition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
