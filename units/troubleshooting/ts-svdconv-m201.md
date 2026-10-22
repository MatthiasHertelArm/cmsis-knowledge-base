---
id: "ts-svdconv-m201"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M201: Tag <…> unknown or not allowed on this level."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M201"
symptoms: ["M201", "Tag <%TAG%> unknown or not allowed on this level."]
symptom_regex: "^Tag <.+?> unknown or not allowed on this level\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Check tag"
summary: "svdconv found an XML element in the SVD file whose tag name is not part of the SVD schema at that nesting level, so it cannot place it."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M201`
`Tag <%TAG%> unknown or not allowed on this level.`

## Cause

svdconv found an XML element in the SVD file whose tag name is not part of the SVD schema at that nesting level, so it cannot place it. The %TAG% in the message is the offending element name as written in the input file.

## Fix

Open the SVD file, locate the element named in the message, and check its spelling and position against the CMSIS-SVD schema. Remove the element or move it to a level where the schema allows it, then rerun svdconv.

## Note

Source lines were not available; the cause and fix rely on the message text and the README cause 'Check tag' only. The schema-level wording is an inference, not confirmed from the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
