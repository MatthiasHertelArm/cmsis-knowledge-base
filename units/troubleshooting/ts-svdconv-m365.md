---
id: "ts-svdconv-m365"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M365: Register '…' (…) (@…) has same address or overlaps '…' (…) (@…) …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M365"
symptoms: ["M365", "Register '%NAME%' (%ACCESS%) (@%ADDRSIZE%) has same address or overlaps '%NAME2%' (%ACCESS2%) (@%ADDRSIZE2%) %LINE%"]
symptom_regex: "^Register '.+?' \\(.+?\\) \\(@.+?\\) has same address or overlaps '.+?' \\(.+?\\) \\(@.+?\\) .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found two registers in the same peripheral whose address ranges are identical or overlap, so one register occupies bytes already used by the other."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M365`
`Register '%NAME%' (%ACCESS%) (@%ADDRSIZE%) has same address or overlaps '%NAME2%' (%ACCESS2%) (@%ADDRSIZE2%) %LINE%`

## Cause

svdconv found two registers in the same peripheral whose address ranges are identical or overlap, so one register occupies bytes already used by the other. The %NAME% and %NAME2% placeholders are the two register names, %ACCESS% and %ACCESS2% their access rights, and %ADDRSIZE% and %ADDRSIZE2% their addresses; %LINE% points to the position in the SVD file. This usually comes from a copy-paste or offset error in the SVD <register> entries (a wrong <addressOffset> or <size>).

## Fix

Open the SVD file at the line given in the message and compare the <addressOffset> and <size> of the two named registers. Correct the offset (or size) of the wrong register so each register has its own address range, then rerun svdconv. If the overlap is intentional, for example a union of alternative views, make sure the SVD uses <alternateRegister> or <alternateGroup> rather than two independent registers.

## Note

Only the message text and the README entry were available; the source trigger lines could not be inspected, so the cause is inferred from the message wording and the README rather than confirmed in SVDConv_Msgs.cpp. The alternateRegister hint is a general SVD convention, not verified against the tool.
