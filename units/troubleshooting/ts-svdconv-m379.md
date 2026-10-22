---
id: "ts-svdconv-m379"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M379: XBin Number '…' too large, skipping evaluation."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M379"
symptoms: ["M379", "XBin Number '%NAME%' too large, skipping evaluation."]
symptom_regex: "^XBin Number '.+?' too large, skipping evaluation\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a binary-, hex- or octal-style number literal in the SVD (for example a field or register value written with an X/B/H prefix) whose value is too large to evaluate, so it could not be converted to an integer."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M379`
`XBin Number '%NAME%' too large, skipping evaluation.`

## Cause

svdconv found a binary-, hex- or octal-style number literal in the SVD (for example a field or register value written with an X/B/H prefix) whose value is too large to evaluate, so it could not be converted to an integer. The %NAME% in the message is the offending expression as it appears in the SVD input.

## Fix

Find the element named in the message in the SVD file and check that its numeric literal is valid and fits the register width; rewrite it as a plain decimal or a correctly sized hex value (for example 0xFFFFFFFF rather than a longer literal), then rerun svdconv. If the value is intentional, the warning is only skipping the evaluation of that expression.

## Note

Trigger and handling were not checked against the source because the clone was not available; the cause and fix are inferred from the message text and the README entry. The message is a warning, so conversion continues without that value.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
