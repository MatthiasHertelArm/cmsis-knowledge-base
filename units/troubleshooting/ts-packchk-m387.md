---
id: "ts-packchk-m387"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M387: Description in '…' is exceeding the recommended 128 (US ASCII) characters."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M387"
symptoms: ["M387", "Description in '%TAG%' is exceeding the recommended 128 (US ASCII) characters."]
symptom_regex: "^Description in '.+?' is exceeding the recommended 128 \\(US ASCII\\) characters\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The text of a <description> element (of the package, a component, device, example and so on) is longer than 128 characters."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:206", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:214-239", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:915-950", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/TestTextExceedsLength/TestVendor.TestTextExceedsLength.pdsc:7"]
---

## Symptom

`M387`
`Description in '%TAG%' is exceeding the recommended 128 (US ASCII) characters.`

## Cause

The text of a <description> element (of the package, a component, device, example and so on) is longer than 128 characters.

## Fix

Shorten the description to at most 128 characters and put longer text into the pack documentation; the message is a recommendation and can be suppressed with -x M387.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:206`
- `tools/packchk/src/CheckFiles.cpp:214-239`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:915-950`
- `tools/packchk/test/data/TestTextExceedsLength/TestVendor.TestTextExceedsLength.pdsc:7`
