---
id: "ts-svdconv-m236"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M236: Expression for <…> '…' not allowed."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M236"
symptoms: ["M236", "Expression for <%TAG%> '%NAME%' not allowed."]
symptom_regex: "^Expression for <.+?> '.+?' not allowed\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv prints this when an SVD element, identified by its tag (%TAG%) and name (%NAME%), contains an expression that the tool does not accept at that position."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M236`
`Expression for <%TAG%> '%NAME%' not allowed.`

## Cause

svdconv prints this when an SVD element, identified by its tag (%TAG%) and name (%NAME%), contains an expression that the tool does not accept at that position. The source lines were not available, so the exact element that triggers it is not confirmed here; the README only says the SVD is incorrect.

## Fix

Open the SVD file at the element named in the message and check its value field. Replace any expression or non-literal text there with a plain numeric literal that the SVD schema allows for that element, then rerun svdconv.

## Note

Source lines were unavailable, so the trigger condition and the set of elements that accept expressions are unverified. The README cause 'Correct SVD' is generic and was not checked against the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
