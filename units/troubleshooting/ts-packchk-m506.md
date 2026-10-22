---
id: "ts-packchk-m506"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M506: RTE Model reports: …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M506"
symptoms: ["M506", "RTE Model reports: %MSG%"]
symptom_regex: "^RTE Model reports: .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk forwards a message produced by the RTE Model (the component/configuration model used by the CMSIS-Pack tooling) and substitutes its text for %MSG%."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M506`
`RTE Model reports: %MSG%`

## Cause

packchk forwards a message produced by the RTE Model (the component/configuration model used by the CMSIS-Pack tooling) and substitutes its text for %MSG%. The underlying problem is whatever the RTE Model reported about the pack's component or configuration definitions, so the exact cause is only visible in the forwarded text itself.

## Fix

Read the text after 'RTE Model reports:' and locate the component, condition, or file it names in the pack's PDSC file. Correct that definition so it is consistent (for example, a condition or component reference that matches an existing definition), then rerun packchk on the pack.

## Note

Only the message text and the trigger name were available; the clone was not provided, so the trigger condition and the handling around it could not be read. The fix is a general direction derived from the message wording, not a verified repair path. Message is documented as not present in the README.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
