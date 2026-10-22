---
id: "ts-packchk-m103"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M103: Internal Error: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M103"
symptoms: ["M103", "Internal Error: %REF%"]
symptom_regex: "^Internal Error: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Contact Arm for clarifications"
summary: "packchk reports this when one of its own internal checks fails, which means the failure is in the tool rather than in the user's pack."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M103`
`Internal Error: %REF%`

## Cause

packchk reports this when one of its own internal checks fails, which means the failure is in the tool rather than in the user's pack. The %REF% placeholder names the internal reference or check that failed. The source lines were not available, so the exact trigger cannot be confirmed here.

## Fix

Re-run packchk on the same pack with the current Open-CMSIS-Pack devtools release. If the error persists, report it to Arm with the full message text, the pack that was checked, and the tool version, as the README suggests contacting Arm.

## Note

Source lines were not provided, so the trigger is inferred from the message text and the README entry only. The README cause is generic and the message is an internal-error category, so the wording above is a reading rather than a confirmed condition.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
