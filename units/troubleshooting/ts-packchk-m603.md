---
id: "ts-packchk-m603"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M603: No license information found"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M603"
symptoms: ["M603", "No license information found"]
symptom_regex: "^No license information found$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints M603 when the pack's PDSC does not contain license information, so the pack's license file or license reference could not be found."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M603`
`No license information found`

## Cause

packchk prints M603 when the pack's PDSC does not contain license information, so the pack's license file or license reference could not be found. Without the source lines, the exact trigger condition cannot be confirmed; the message text indicates the check looks for license information in the pack description.

## Fix

Add license information to the pack: reference a license file in the PDSC (for example a license element pointing to a LICENSE file shipped in the pack root) and make sure that file is included in the pack. Then rerun packchk.

## Note

Only the message text and source file name were provided; the trigger line was not available, so the specific PDSC element checked is not confirmed. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
