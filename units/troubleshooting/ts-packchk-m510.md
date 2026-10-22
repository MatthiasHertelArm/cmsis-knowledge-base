---
id: "ts-packchk-m510"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M510: Xerxes reports: …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M510"
symptoms: ["M510", "Xerxes reports: %MSG%"]
symptom_regex: "^Xerxes reports: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints this warning when it forwards a message from its embedded Xerxes checker, which is the library that validates PDSC content; %MSG% is the text Xerxes produced for the specific problem in the pack description."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M510`
`Xerxes reports: %MSG%`

## Cause

packchk prints this warning when it forwards a message from its embedded Xerxes checker, which is the library that validates PDSC content; %MSG% is the text Xerxes produced for the specific problem in the pack description. The exact condition behind each Xerxes message cannot be determined here because the source lines were not available.

## Fix

Read the text that follows 'Xerxes reports:' in the build log, locate the element or attribute it names in the .pdsc file, correct that entry so it matches the schema or the rule it describes, and rerun packchk.

## Note

Source lines were not provided, so the trigger and the Xerxes relation are inferred from the message text alone. The message is not documented in the README. The specific fix depends on the Xerxes text in %MSG%, which the entry cannot enumerate.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
