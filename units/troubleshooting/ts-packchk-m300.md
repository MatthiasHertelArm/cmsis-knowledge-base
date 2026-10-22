---
id: "ts-packchk-m300"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M300: … must use '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M300"
symptoms: ["M300", "%TAG% must use '%URL%'"]
symptom_regex: "^.+? must use '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "An element text or attribute value in the PDSC contains 'http://', for example <url>, <repository>, the url of a <release>, the name of a <book> or <file>, a board orderForm or an <image> link. %TAG% is the element name …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:108", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:246-269", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:41-56", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:826-855", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/TestUrlHttps/TestVendor.TestUrlHttps.pdsc:5-65"]
---

## Symptom

`M300`
`%TAG% must use '%URL%'`

## Cause

An element text or attribute value in the PDSC contains 'http://', for example <url>, <repository>, the url of a <release>, the name of a <book> or <file>, a board orderForm or an <image> link. %TAG% is the element name for element text, or the attribute name; packchk wants 'https://'.

## Fix

Change each reported link from http:// to https:// and check that the https address works, e.g. <url>https://www.myvendor.com/pack/</url>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:108`
- `tools/packchk/src/CheckFiles.cpp:246-269`
- `tools/packchk/src/CheckFiles.cpp:41-56`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:826-855`
- `tools/packchk/test/data/TestUrlHttps/TestVendor.TestUrlHttps.pdsc:5-65`
