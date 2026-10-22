---
id: "ts-packchk-m207"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M207: PDSC file name mismatch! Expected: '….pdsc' Actual : '….pdsc'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M207"
symptoms: ["M207", "PDSC file name mismatch!   Expected: '%PDSC1%.pdsc'   Actual  : '%PDSC2%.pdsc'"]
symptom_regex: "^PDSC file name mismatch!   Expected: '.+?\\.pdsc'   Actual  : '.+?\\.pdsc'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The PDSC file expected has not been found. Rename or exchange the PDSC file."
summary: "packchk compares the name of the PDSC file with the pack name recorded inside the pack (the Name and Version of the pack, which the PDSC file name is expected to follow as <Vendor>.<Name>.pdsc)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M207`
`PDSC file name mismatch!   Expected: '%PDSC1%.pdsc'   Actual  : '%PDSC2%.pdsc'`

## Cause

packchk compares the name of the PDSC file with the pack name recorded inside the pack (the Name and Version of the pack, which the PDSC file name is expected to follow as <Vendor>.<Name>.pdsc). When the file on disk is named differently from what the pack's own name implies, the tool prints M207 with the expected name in %PDSC1% and the actual file name in %PDSC2%. The source lines were not available, so this is inferred from the message text and the README rather than read from the trigger.

## Fix

Rename the PDSC file so that its base name matches the expected name shown in the message, for example rename the file so it reads %PDSC1%.pdsc, or correct the vendor and pack name in the PDSC file so that the expected name becomes the file name you actually use. Then run packchk again.

## Note

Source lines were not available; the cause is taken from the message text and the README. The README describes the expected file as not found, which is only partly consistent with the message wording, which reports a name mismatch between expected and actual file names. The fix relies on the README's suggestion to rename or exchange the file.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
