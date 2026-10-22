---
id: "ts-packchk-m387"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M387: Description in '…' is exceeding the recommended 128 (US ASCII) characters."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M387"
symptoms: ["M387", "Description in '%TAG%' is exceeding the recommended 128 (US ASCII) characters."]
symptom_regex: "^Description in '.+?' is exceeding the recommended 128 \\(US ASCII\\) characters\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk checks the length of a description text in the PDSC file (the element named by the variable part %TAG%) and warns when it exceeds the recommended 128 US ASCII characters."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M387`
`Description in '%TAG%' is exceeding the recommended 128 (US ASCII) characters.`

## Cause

packchk checks the length of a description text in the PDSC file (the element named by the variable part %TAG%) and warns when it exceeds the recommended 128 US ASCII characters. The text is too long for the recommended limit, and it is a warning only, not a hard error.

## Fix

Shorten the description text of the element named in the message so that it is at most 128 US ASCII characters, moving detail into documentation elsewhere if needed. Remove non-ASCII characters from that text if they count toward the limit.

## Note

Source lines were not available, so the trigger and the handling are inferred from the message text alone; the exact check and which element %TAG% names could not be verified. README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
