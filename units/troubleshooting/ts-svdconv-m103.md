---
id: "ts-svdconv-m103"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M103: Internal Error: …"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M103"
symptoms: ["M103", "Internal Error: %REF%"]
symptom_regex: "^Internal Error: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Please contact support."
summary: "svdconv prints this message when it reaches an internal consistency check that should never fail; the %REF% placeholder names the internal reference that was involved."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M103`
`Internal Error: %REF%`

## Cause

svdconv prints this message when it reaches an internal consistency check that should never fail; the %REF% placeholder names the internal reference that was involved. The source lines are not available here, so the specific condition cannot be confirmed and the cause is inferred from the message text alone.

## Fix

Re-run svdconv with the same input and command line to confirm the failure is reproducible. If it is, collect the full message, the SVD or PDSC file involved, and the svdconv version, then report it to the CMSIS devtools project (the README asks to contact support). No user-side change is known to resolve an internal error.

## Note

Source lines were not provided, so the trigger was not read. The README gives only 'Please contact support' as cause, so there is no documented user-side fix. Confidence is capped at medium by the task rules and is set to low because the trigger itself is unverified.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
