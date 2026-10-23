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
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "No <interrupt> in the device has a <value> below 16. svdconv takes this as a sign that interrupts were numbered by exception number (first device interrupt = 16) instead of from 0."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:658", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:667", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:679", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:680", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:174"]
---

## Symptom

`M355`
`No Interrupts found on pos. 0..15. External (Vendor-)Interrupts possibly defined on position 16+. External Interrupts must start on position 0`

## Cause

No <interrupt> in the device has a <value> below 16. svdconv takes this as a sign that interrupts were numbered by exception number (first device interrupt = 16) instead of from 0.

## Fix

Number device interrupts from 0, i.e. subtract 16 from exception numbers. If the device really has no interrupt numbered below 16, the message can be ignored.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:658`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:667`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:679`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:680`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:174`
