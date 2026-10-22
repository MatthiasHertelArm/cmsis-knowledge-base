---
id: "ts-packchk-m605"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M605: Required Dcore '…' feature '…' not defined"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M605"
symptoms: ["M605", "Required Dcore '%NAME%' feature '%NAME2%' not defined"]
symptom_regex: "^Required Dcore '.+?' feature '.+?' not defined$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints this warning when a device's Dcore definition in the PDSC lists a required feature by name, and that feature is not defined under the Dcore entry it refers to."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text M605 only; trigger lines not available)"]
---

## Symptom

`M605`
`Required Dcore '%NAME%' feature '%NAME2%' not defined`

## Cause

packchk prints this warning when a device's Dcore definition in the PDSC lists a required feature by name, and that feature is not defined under the Dcore entry it refers to. The %NAME% part is the core name (for example a Dcore id) and %NAME2% is the feature name that the check could not find. The source lines were not available, so this reading is based on the message text alone.

## Fix

Open the PDSC file and look at the Dcore entry named in the message. Either add the missing feature definition under that Dcore, or correct the spelling of the feature name so it matches a feature the Dcore actually defines. Then rerun packchk on the pack.

## Note

README does not document M605. The trigger condition is inferred from the message wording, not read from the source. Verify the exact check in PackChk_Msgs.cpp before relying on the fix.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text M605 only; trigger lines not available)`
