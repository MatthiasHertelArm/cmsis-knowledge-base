---
id: "ts-svdconv-m357"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M357: Core Interrupts found. Interrupt Numbers are wrong. Internal Interrupts must not be described, …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M357"
symptoms: ["M357", "Core Interrupts found. Interrupt Numbers are wrong. Internal Interrupts must not be described, External Interrupts must start at 0."]
symptom_regex: "^Core Interrupts found\\. Interrupt Numbers are wrong\\. Internal Interrupts must not be described, External Interrupts must start at 0\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:176", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:351", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:674", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:680"]
---

## Symptom

`M357`
`Core Interrupts found. Interrupt Numbers are wrong. Internal Interrupts must not be described, External Interrupts must start at 0.`

## Cause

_open: to be written in the review_

## Fix

_open: to be written in the review_

## Note

No LogMsg call for this code exists in svdconv at 30f5e81; the related checks raised today are M354 (core exception listed as interrupt) and M355 (no interrupt below 16).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:176`
- `tools/svdconv/SVDConv/README.md:351`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:674`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:680`
