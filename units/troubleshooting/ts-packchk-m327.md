---
id: "ts-packchk-m327"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M327: Path is not conformant: '…': Backslashes are not recommended, use forward slashes."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M327"
symptoms: ["M327", "Path is not conformant: '%PATH%':   Backslashes are not recommended, use forward slashes."]
symptom_regex: "^Path is not conformant: '.+?':   Backslashes are not recommended, use forward slashes\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Paths to files should adhere to the POSIX standard using forward slashes (/)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:143", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/RteModelReader.cpp:57-63", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:163-169", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:453-496", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/TestLicense/TestVendor.TestPackLicense.pdsc:8", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:168"]
---

## Symptom

`M327`
`Path is not conformant: '%PATH%':   Backslashes are not recommended, use forward slashes.`

## Cause

Paths to files should adhere to the POSIX standard using forward slashes (/).

## Fix

Replace the backslashes with forward slashes, e.g. Device/Include/device.h.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:143`
- `tools/packchk/src/RteModelReader.cpp:57-63`
- `tools/packchk/src/ValidateSyntax.cpp:163-169`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:453-496`
- `tools/packchk/test/data/TestLicense/TestVendor.TestPackLicense.pdsc:8`
- `tools/packchk/README.md:168`
