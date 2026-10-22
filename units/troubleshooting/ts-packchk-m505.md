---
id: "ts-packchk-m505"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M505: RTE Model reports: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M505"
symptoms: ["M505", "RTE Model reports: %MSG%"]
symptom_regex: "^RTE Model reports: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk forwards a message produced by the RTE Model (the component/configuration model used by the CMSIS-Pack tooling) and prints its text in place of %MSG%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M505`
`RTE Model reports: %MSG%`

## Cause

packchk forwards a message produced by the RTE Model (the component/configuration model used by the CMSIS-Pack tooling) and prints its text in place of %MSG%. The variable part is the RTE Model's own diagnostic text, which describes the specific problem found in the pack's component or configuration data; the exact wording cannot be determined without the source lines.

## Fix

Read the text that follows 'RTE Model reports:' in the log, which names the underlying problem, and correct the PDSC component, condition or bundle definitions it refers to, then re-run packchk. If the text is unclear, check the component and condition definitions of the pack against the CMSIS-Pack specification.

## Note

Source lines were not available, so the trigger and the meaning of %MSG% are not verified from code; the cause and fix are inferred from the message text alone. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
