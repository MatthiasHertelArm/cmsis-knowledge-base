---
id: "ts-svdconv-m339"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M339: Register '…' (…) (@…) has same address or overlaps '…' (…) (@…) …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M339"
symptoms: ["M339", "Register '%NAME%' (%ACCESS%) (@%ADDRSIZE%) has same address or overlaps '%NAME2%' (%ACCESS2%) (@%ADDRSIZE2%) %LINE%"]
symptom_regex: "^Register '.+?' \\(.+?\\) \\(@.+?\\) has same address or overlaps '.+?' \\(.+?\\) \\(@.+?\\) .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found two registers in the input SVD whose address ranges collide: the register named in the message (%NAME%) and the register %NAME2% occupy the same address or overlap each other."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; trigger lines not available)"]
---

## Symptom

`M339`
`Register '%NAME%' (%ACCESS%) (@%ADDRSIZE%) has same address or overlaps '%NAME2%' (%ACCESS2%) (@%ADDRSIZE2%) %LINE%`

## Cause

svdconv found two registers in the input SVD whose address ranges collide: the register named in the message (%NAME%) and the register %NAME2% occupy the same address or overlap each other. This usually comes from an SVD in which two register entries share an offset, or in which a register array or cluster expands to addresses already used by another register. The source lines were not available, so this reading is based on the message text alone.

## Fix

Open the SVD file and locate both registers named in the message. Check their addressOffset values and, if they belong to a register array or cluster, their dim, dimIncrement and size settings. Correct the offset or the array settings so that each register has its own address range, then run svdconv again.

## Note

Source lines were not available. The message text shows the two registers and their addresses, but the exact trigger condition in the source is not confirmed. The message also carries a %LINE% field, which likely gives the SVD line number of the conflict; check it when locating the registers.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp (message text only; trigger lines not available)`
