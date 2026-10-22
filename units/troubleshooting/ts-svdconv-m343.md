---
id: "ts-svdconv-m343"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M343: … '…' (@…) has same address as '…' …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M343"
symptoms: ["M343", "%LEVEL% '%NAME%' (@%ADDR%) has same address as '%NAME2%' %LINE%"]
symptom_regex: "^.+? '.+?' \\(@.+?\\) has same address as '.+?' .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found two register or cluster entries in the input SVD that resolve to the same address, so one would overwrite the other in the generated output."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message definition for M343; exact line not available)"]
---

## Symptom

`M343`
`%LEVEL% '%NAME%' (@%ADDR%) has same address as '%NAME2%' %LINE%`

## Cause

svdconv found two register or cluster entries in the input SVD that resolve to the same address, so one would overwrite the other in the generated output. The %LEVEL%, %NAME% and %NAME2% placeholders name the two conflicting elements, %ADDR% is the shared address, and %LINE% gives the source location in the SVD file. The README cause text was not checked against source because the clone is not available.

## Fix

Open the SVD file at the line reported in the message and correct the offset or addressOffset of one of the two named elements (or of their parent cluster or peripheral base address) so each register has a distinct address. If the overlap is intentional, for example a union of registers, model it with a cluster or an alternate register rather than two independent registers at the same offset.

## Note

Answered from the message text and the README entry only; the source clone was not available, so the trigger condition and the exact cause wording are inferred from the message and not confirmed in the code. The fix assumes the duplicate is an input error rather than an intended overlay.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message definition for M343; exact line not available)`
