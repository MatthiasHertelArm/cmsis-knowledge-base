---
id: "ts-svdconv-m205"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M205: Tag <…> empty"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M205"
symptoms: ["M205", "Tag <%TAG%> empty"]
symptom_regex: "^Tag <.+?> empty$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Assign value to tag."
summary: "The SVD input has an XML element whose text content is empty, and the element is one that svdconv reads and expects to hold a value."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M205`
`Tag <%TAG%> empty`

## Cause

The SVD input has an XML element whose text content is empty, and the element is one that svdconv reads and expects to hold a value. The %TAG% placeholder is the name of that element.

## Fix

Open the SVD file at the tag named in the message and give it a value, or remove the empty element if the schema allows it. Then rerun svdconv.

## Note

Source lines were not available; the cause and fix come from the message text and the README entry ('Assign value to tag'), not from the trigger code, so verify the exact condition before relying on it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
