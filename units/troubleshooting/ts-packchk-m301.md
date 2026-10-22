---
id: "ts-packchk-m301"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M301: Checking Pack URL of PDSC file failed: Expected URL : '…' Package URL : '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M301"
symptoms: ["M301", "Checking Pack URL of PDSC file failed:   Expected URL : '%URL1%'   Package  URL : '%URL2%'"]
symptom_regex: "^Checking Pack URL of PDSC file failed:   Expected URL : '.+?'   Package  URL : '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The URL specified in the package does not match the value entered for comparison in option `-u`. Check for possible misspellings in both URLs. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url)."
summary: "packchk compares the URL given with its -u option against the url element of the package description in the PDSC file."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available for this entry)"]
---

## Symptom

`M301`
`Checking Pack URL of PDSC file failed:   Expected URL : '%URL1%'   Package  URL : '%URL2%'`

## Cause

packchk compares the URL given with its -u option against the url element of the package description in the PDSC file. When these two values differ, the tool prints M301 with the expected URL (the -u value) in place of %URL1% and the URL found in the PDSC in place of %URL2%. The README attributes this to a mismatch, possibly a misspelling in one of the two URLs.

## Fix

Compare the URL passed to packchk with -u against the url element in the PDSC file and make them identical, correcting any misspelling or differing trailing characters in either of them.

## Note

Trigger and handling are inferred from the message text and README only, since the clone is not available. The source lines for the comparison were not checked.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp (message text only; source lines not available for this entry)`
