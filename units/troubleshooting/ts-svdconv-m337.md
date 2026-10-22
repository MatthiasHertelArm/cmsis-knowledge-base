---
id: "ts-svdconv-m337"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M337: … '…' already defined …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M337"
symptoms: ["M337", "%LEVEL% '%NAME%' already defined %LINE%"]
symptom_regex: "^.+? '.+?' already defined .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a second definition of a named SVD element (the %LEVEL% placeholder names the kind of element, the %NAME% placeholder its name) in the same scope, so the duplicate name is ambiguous."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M337`
`%LEVEL% '%NAME%' already defined %LINE%`

## Cause

svdconv found a second definition of a named SVD element (the %LEVEL% placeholder names the kind of element, the %NAME% placeholder its name) in the same scope, so the duplicate name is ambiguous. The %LINE% placeholder points to the line where the earlier definition sits. The source lines were not available, so this reading is inferred from the message text alone.

## Fix

Open the SVD file at the line given in the message and at the earlier definition it refers to. Rename one of the two entries, or remove the duplicate, so that each register, field or peripheral name is unique within its scope, then run svdconv again.

## Note

Trigger and handling were not checked against the source, since the clone was not available. The exact scopes that count as duplicates (for example peripheral versus register level) are not confirmed here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
