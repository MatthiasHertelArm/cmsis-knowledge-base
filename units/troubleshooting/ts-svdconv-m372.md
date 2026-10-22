---
id: "ts-svdconv-m372"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M372: … <…> '…' already defined …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M372"
symptoms: ["M372", "%LEVEL% <%TAG%> '%NAME%' already defined %LINE%"]
symptom_regex: "^.+? <.+?> '.+?' already defined .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "The SVD file defines the same element more than once in the same scope, for example two peripherals or registers with an identical name under one parent. svdconv reports the second occurrence as a duplicate, with the tag name …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M372`
`%LEVEL% <%TAG%> '%NAME%' already defined %LINE%`

## Cause

The SVD file defines the same element more than once in the same scope, for example two peripherals or registers with an identical name under one parent. svdconv reports the second occurrence as a duplicate, with the tag name (%TAG%), the element name (%NAME%) and the line where the earlier definition sits (%LINE%). The exact trigger condition could not be checked against the source, so this is inferred from the message text.

## Fix

Open the SVD file at the line named in the message and rename or remove the duplicate element so that each name is unique within its parent, then run svdconv again. Check the same tag and name in the other occurrence as well.

## Note

Source lines were not available; the cause and fix rest on the message text and the README entry, not on the trigger code. The README is said to document this message, but its text was not provided to me.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
