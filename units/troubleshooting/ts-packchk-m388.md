---
id: "ts-packchk-m388"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M388: Unsupported character(s) found in '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M388"
symptoms: ["M388", "Unsupported character(s) found in '%NAME%'"]
symptom_regex: "^Unsupported character\\(s\\) found in '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints this warning when a name taken from the pack (the %NAME% part, for example a component, device or file name in the PDSC) contains characters outside the set it accepts."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M388`
`Unsupported character(s) found in '%NAME%'`

## Cause

packchk prints this warning when a name taken from the pack (the %NAME% part, for example a component, device or file name in the PDSC) contains characters outside the set it accepts. The exact trigger condition could not be checked because the source clone was not available, so this reading comes from the message text alone.

## Fix

Find the element named in the message in the PDSC and rename it so it uses only plain letters, digits and the separators the schema allows (for example avoid spaces and special punctuation), then rerun packchk.

## Note

Source lines were not provided, so the trigger condition and the exact allowed character set are unverified. The message is not documented in the README. The %NAME% placeholder is not resolved in the message text, so the offending name is only visible in the actual build log.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
