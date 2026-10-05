---
id: "ts-packchk-m207"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M207: PDSC file name mismatch!   Expected"
status: "draft"
tool: "packchk"
severity: "error"
code: "M207"
symptoms: ["M207", "PDSC file name mismatch!   Expected: '%PDSC1%.pdsc'   Actual  : '%PDSC2%.pdsc'"]
symptom_regex: "^PDSC file name mismatch!   Expected: '.+?\\.pdsc'   Actual  : '.+?\\.pdsc'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M207`
`PDSC file name mismatch!   Expected: '%PDSC1%.pdsc'   Actual  : '%PDSC2%.pdsc'`

## Cause

The PDSC file expected has not been found. Rename or exchange the PDSC file.

## Fix

_siehe Cause_
