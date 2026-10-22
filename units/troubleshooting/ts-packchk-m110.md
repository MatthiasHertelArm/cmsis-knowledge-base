---
id: "ts-packchk-m110"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M110: Verifying RTE Model failed"
status: "draft"
tool: "packchk"
severity: "error"
code: "M110"
symptoms: ["M110", "Verifying RTE Model failed"]
symptom_regex: "^Verifying RTE Model failed$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Contact Arm for clarifications"
summary: "packchk reports M110 when verification of the RTE model of the pack fails, but the source lines for the trigger were not available, so the specific condition that causes it cannot be confirmed."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M110`
`Verifying RTE Model failed`

## Cause

packchk reports M110 when verification of the RTE model of the pack fails, but the source lines for the trigger were not available, so the specific condition that causes it cannot be confirmed. The README gives no cause beyond a pointer to contact Arm.

## Fix

Re-run packchk with the same pack and check the earlier messages in the same log for the component or condition that the RTE model check rejected; correct the reported component definitions in the PDSC and run packchk again.

## Note

Source lines were not available, so the trigger and handling are unverified; the fix is a generic check, not a source-confirmed remedy. The README cause is only a contact pointer, so the message text is the only confirmed content.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
