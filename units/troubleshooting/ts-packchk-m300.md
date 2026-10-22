---
id: "ts-packchk-m300"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M300: … must use '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M300"
symptoms: ["M300", "%TAG% must use '%URL%'"]
symptom_regex: "^.+? must use '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints this warning when a PDSC element named by %TAG% carries a URL that does not match the form the tool expects for that element, so the value of %URL% is the required form it compares against."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M300`
`%TAG% must use '%URL%'`

## Cause

packchk prints this warning when a PDSC element named by %TAG% carries a URL that does not match the form the tool expects for that element, so the value of %URL% is the required form it compares against. The exact trigger condition could not be read because the clone is not available, so this is inferred from the message text alone.

## Fix

Open the PDSC file, find the element named in the message, and change its URL text to the form given by %URL% (for example, make sure it ends with a trailing slash or uses the required scheme, as the message states). Then rerun packchk.

## Note

Source lines were not provided, so the trigger and the exact URL rule were not verified; the cause and fix rely on the message text only. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
