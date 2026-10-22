---
id: "ts-svdconv-m237"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M237: Nameless … must have <…>."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M237"
symptoms: ["M237", "Nameless %LEVEL% must have <%TAG%>."]
symptom_regex: "^Nameless .+? must have <.+?>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "svdconv prints this when an SVD element that is meant to carry a name (for example a peripheral, register or field, given by %LEVEL%) has no <name> child, while the tag named by %TAG% is required for it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)"]
---

## Symptom

`M237`
`Nameless %LEVEL% must have <%TAG%>.`

## Cause

svdconv prints this when an SVD element that is meant to carry a name (for example a peripheral, register or field, given by %LEVEL%) has no <name> child, while the tag named by %TAG% is required for it. The SVD input is missing that name element at the reported level. The README gives only 'Correct SVD.' as the cause, so the exact element is taken from the message text and not verified against source lines.

## Fix

Open the SVD file at the element the message refers to and add the missing <name> element (the %TAG% in the message), making sure the name is not empty. Then run svdconv again on the corrected file.

## Note

Source lines were not provided, so the trigger condition and the exact element are inferred from the message wording and the README. Message text suggests the check is about a missing name at a given SVD level.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (trigger not available in the clone; message text only)`
