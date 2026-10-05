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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The PDSC file expected has not been found. Rename or exchange the PDSC file."
summary: "The PDSC file name is not <vendor>.<name>.pdsc as built from the <vendor> and <name> elements of the PDSC (exact, case-sensitive comparison)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:91-93", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:335-341", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:136"]
---

## Symptom

`M207`
`PDSC file name mismatch!   Expected: '%PDSC1%.pdsc'   Actual  : '%PDSC2%.pdsc'`

## Cause

The PDSC file name is not <vendor>.<name>.pdsc as built from the <vendor> and <name> elements of the PDSC (exact, case-sensitive comparison). 'Expected' shows the name built from the elements, 'Actual' the file name.

## Fix

Rename the PDSC to <vendor>.<name>.pdsc, or correct <vendor> or <name>, e.g. file MyVendor.MyPack.pdsc with <vendor>MyVendor</vendor> and <name>MyPack</name>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:91-93`
- `tools/packchk/src/ValidateSyntax.cpp:335-341`
- `tools/packchk/README.md:136`
