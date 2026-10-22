---
id: "ts-svdconv-m368"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M368: … '…' (@…) has same address as '…' …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M368"
symptoms: ["M368", "%LEVEL% '%NAME%' (@%ADDR%) has same address as '%NAME2%' %LINE%"]
symptom_regex: "^.+? '.+?' \\(@.+?\\) has same address as '.+?' .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found two register or cluster entries in the input SVD that resolve to the same address."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M368`
`%LEVEL% '%NAME%' (@%ADDR%) has same address as '%NAME2%' %LINE%`

## Cause

svdconv found two register or cluster entries in the input SVD that resolve to the same address. The %NAME% and %NAME2% placeholders are the two colliding entries, %ADDR% is the shared address, %LEVEL% says whether it is a register or a cluster, and %LINE% gives the position in the SVD file. Because the source was not available, the exact trigger condition is inferred from the message wording and not verified in code.

## Fix

Open the SVD file at the reported line and check the offsets of the two named entries, including any dim/dimIncrement or cluster base address that moves them. Correct the addressOffset or cluster offset so each register has its own address, or remove the duplicate if it was copied by mistake.

## Note

The clone was unavailable, so the trigger and the handling were not read from source; the cause is derived from the message text and the README, which documents this message. Overlapping but not identical addresses may be reported differently and are not covered here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
