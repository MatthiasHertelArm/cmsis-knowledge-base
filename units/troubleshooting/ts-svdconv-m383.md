---
id: "ts-svdconv-m383"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M383: Number of PMU Event Counters set but PMU present not set"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M383"
symptoms: ["M383", "Number of PMU Event Counters set but PMU present not set"]
symptom_regex: "^Number of PMU Event Counters set but PMU present not set$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD device description sets the number of PMU event counters (numEventCounters or the equivalent PMU element field) but does not mark the PMU as present (the PMU-present flag is not set). svdconv reports the inconsistency as M383 because …"
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M383`
`Number of PMU Event Counters set but PMU present not set`

## Cause

The SVD device description sets the number of PMU event counters (numEventCounters or the equivalent PMU element field) but does not mark the PMU as present (the PMU-present flag is not set). svdconv reports the inconsistency as M383 because counter settings are only meaningful when the PMU is declared present. The exact XML element names were not available in the provided source lines, so this reading rests on the message text alone.

## Fix

Open the SVD file and find the PMU-related fields in the CPU section. Either set the PMU-present flag to true (the field that declares the PMU present) or remove the event counter count if the device has no PMU. Then rerun svdconv on the corrected file.

## Note

Source lines were not available; the trigger location and exact SVD element names are unverified. Treat the element names as to be checked against the CMSIS-SVD schema.
