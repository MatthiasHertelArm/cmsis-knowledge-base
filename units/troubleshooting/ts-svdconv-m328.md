---
id: "ts-svdconv-m328"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M328: … '…' has no Registers, ignoring …."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M328"
symptoms: ["M328", "%LEVEL% '%NAME%' has no Registers, ignoring %LEVEL%."]
symptom_regex: "^.+? '.+?' has no Registers, ignoring .+?\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found a peripheral or cluster in the input SVD that contains no register elements, so it skips that level."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M328`
`%LEVEL% '%NAME%' has no Registers, ignoring %LEVEL%.`

## Cause

svdconv found a peripheral or cluster in the input SVD that contains no register elements, so it skips that level. The %LEVEL% and %NAME% placeholders are the element kind (for example peripheral or cluster) and the name of the empty element in the SVD file. Source lines were not available, so this reading comes from the message text alone.

## Fix

Open the SVD file, find the element named in the message, and check whether its <registers> block is missing or empty. If the device description is meant to define registers there, add them or correct the element name. If the element is intentionally empty, the warning can be accepted because svdconv ignores it.

## Note

Trigger and handling were not checked against the source because the clone was not available; the cause and fix are inferred from the message wording and should be confirmed.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
