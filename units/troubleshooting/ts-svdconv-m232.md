---
id: "ts-svdconv-m232"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M232: Tag <…> name '…' must not have specifier '…'. Ignoring entry."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M232"
symptoms: ["M232", "Tag <%TAG%> name '%NAME%' must not have specifier '%CHAR%'. Ignoring entry."]
symptom_regex: "^Tag <.+?> name '.+?' must not have specifier '.+?'\\. Ignoring entry\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv found a name in an SVD element that contains a character the tool does not allow for that tag, so it discards the entry."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M232`
`Tag <%TAG%> name '%NAME%' must not have specifier '%CHAR%'. Ignoring entry.`

## Cause

svdconv found a name in an SVD element that contains a character the tool does not allow for that tag, so it discards the entry. The %TAG% and %NAME% parts identify the element and its name, and %CHAR% is the offending character. The README only states that the SVD is incorrect, and the source lines were not available to confirm the exact check.

## Fix

Open the SVD file at the element named in the message and remove the forbidden character from that name, then rerun svdconv. Check the SVD against the CMSIS-SVD schema if unsure which characters are allowed.

## Note

Trigger and handling were not verified against source lines; the cause is inferred from the message text and the README's brief cause. The message text says 'Ignoring entry', so the tool continues but drops that entry.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
