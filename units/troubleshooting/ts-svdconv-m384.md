---
id: "ts-svdconv-m384"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M384: Number of PMU Event Counters (found val: '…') not set or outside range [2..31]. Ignoring PMU entry."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M384"
symptoms: ["M384", "Number of PMU Event Counters (found val: '%NUM%') not set or outside range [2..31]. Ignoring PMU entry."]
symptom_regex: "^Number of PMU Event Counters \\(found val: '.+?'\\) not set or outside range \\[2\\.\\.31\\]\\. Ignoring PMU entry\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a PMU entry in the SVD (Cortex-M PMU description) whose number of PMU event counters is either missing or outside the accepted range 2 to 31."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M384`
`Number of PMU Event Counters (found val: '%NUM%') not set or outside range [2..31]. Ignoring PMU entry.`

## Cause

svdconv found a PMU entry in the SVD (Cortex-M PMU description) whose number of PMU event counters is either missing or outside the accepted range 2 to 31. The value shown in the message is the one that was read from the SVD. Because the value is invalid, svdconv ignores the PMU entry rather than stopping the conversion.

## Fix

Open the SVD file and check the PMU element for the number of event counters (the value must be an integer from 2 to 31). Correct the value to the number your device's PMU actually provides, then run svdconv again. If the PMU is not needed for your build, the message can be left as is because the entry is simply skipped.

## Note

Trigger and range are taken from the message text only; the clone was not available, so the exact SVD element name and the handling code were not checked. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
