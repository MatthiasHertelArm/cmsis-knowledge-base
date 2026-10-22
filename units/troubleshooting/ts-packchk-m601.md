---
id: "ts-packchk-m601"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M601: '…' missing on '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M601"
symptoms: ["M601", "'%TAG%' missing on '%TAG2%'"]
symptom_regex: "^'.+?' missing on '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk found that a required element or attribute named by the first placeholder is absent from the element named by the second placeholder inside the PDSC file being checked."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M601`
`'%TAG%' missing on '%TAG2%'`

## Cause

packchk found that a required element or attribute named by the first placeholder is absent from the element named by the second placeholder inside the PDSC file being checked. The exact tag names are only in the message text, so the specific element is not confirmed from source here.

## Fix

Open the PDSC file named in the packchk output, go to the element named in the message (the second placeholder), and add the missing child element or attribute with the name given by the first placeholder, following the CMSIS Pack schema for that element. Then re-run packchk.

## Note

Source lines were not available, so the trigger condition could not be read. The cause and fix are inferred from the message text alone and should be verified against the trigger in PackChk_Msgs.cpp. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
