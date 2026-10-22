---
id: "ts-packchk-m321"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M321: DS5 project requires '.project' file."
status: "draft"
tool: "packchk"
severity: "error"
code: "M321"
symptoms: ["M321", "DS5 project requires '.project' file."]
symptom_regex: "^DS5 project requires '\\.project' file\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk checks that a pack which contains DS5 project material ships a '.project' file alongside it; the message reports that such a DS5 project is present but its '.project' file is missing."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M321`
`DS5 project requires '.project' file.`

## Cause

packchk checks that a pack which contains DS5 project material ships a '.project' file alongside it; the message reports that such a DS5 project is present but its '.project' file is missing. The trigger source lines were not provided, so this reading rests on the message text alone.

## Fix

Add the Eclipse-style '.project' file that DS5 expects next to the project's other files in the pack, then re-run packchk. If the pack does not ship a DS5 project, remove the DS5 project entries from the pack description.

## Note

Source lines were not available; the trigger condition and the fix are inferred from the message wording and should be verified against PackChk_Msgs.cpp before relying on them.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
