---
id: "ts-packchk-m604"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M604: Currently no Dcore feature check for '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M604"
symptoms: ["M604", "Currently no Dcore feature check for '%NAME%'"]
symptom_regex: "^Currently no Dcore feature check for '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints this warning when a Dcore (device core) feature check is requested for a named feature, but no check for that feature has been implemented in the tool yet."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M604`
`Currently no Dcore feature check for '%NAME%'`

## Cause

packchk prints this warning when a Dcore (device core) feature check is requested for a named feature, but no check for that feature has been implemented in the tool yet. The %NAME% placeholder is the feature name the check was asked for, so the message reflects a limitation of the checker rather than an error in the user's pack.

## Fix

No change to the pack is indicated by the message alone. Check whether the flagged feature is actually required for the device, and verify the Dcore settings in the PDSC against the device documentation by hand, since packchk does not validate that feature.

## Note

Only the message text and the source file name were available; the trigger lines were not supplied, so the cause is inferred from the wording of the message. Treat the reading as unverified until the trigger condition is checked in the source.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
