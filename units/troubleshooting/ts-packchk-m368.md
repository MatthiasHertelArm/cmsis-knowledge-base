---
id: "ts-packchk-m368"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M368: Cannot check '…'…"
status: "draft"
tool: "packchk"
severity: "error"
code: "M368"
symptoms: ["M368", "Cannot check '%NAME%'%MSG%"]
symptom_regex: "^Cannot check '.+?'.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A <compatibleDevice> element of a <board> has no Dname attribute (for example it only gives Dfamily or DsubFamily), so packchk cannot look the device up; the message reads \"Cannot check 'compatibleDevice', no 'Dname' could be calculated\"."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:187", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1783-1789"]
---

## Symptom

`M368`
`Cannot check '%NAME%'%MSG%`

## Cause

A <compatibleDevice> element of a <board> has no Dname attribute (for example it only gives Dfamily or DsubFamily), so packchk cannot look the device up; the message reads "Cannot check 'compatibleDevice', no 'Dname' could be calculated".

## Fix

Give every <compatibleDevice> a Dname and Dvendor, one element per device, e.g. <compatibleDevice deviceIndex="0" Dvendor="ARM:82" Dname="ARMCM3"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:187`
- `tools/packchk/src/ValidateSyntax.cpp:1783-1789`
