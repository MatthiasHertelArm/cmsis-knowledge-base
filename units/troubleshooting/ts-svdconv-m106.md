---
id: "ts-svdconv-m106"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M106: Command '…' failed: …: …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M106"
symptoms: ["M106", "Command '%NAME%' failed: %NUM%: %MSG%"]
symptom_regex: "^Command '.+?' failed: .+?: .*$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:43", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md:224"]
---

## Symptom

`M106`
`Command '%NAME%' failed: %NUM%: %MSG%`

## Cause

_open: to be written in the review_

## Fix

_open: to be written in the review_

## Note

No LogMsg call for this code exists in svdconv at 30f5e81; the code is only defined in the message table, so this version cannot print it. packchk reuses the number M106 for a different message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence unknown, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:43`
- `tools/svdconv/SVDConv/README.md:224`
