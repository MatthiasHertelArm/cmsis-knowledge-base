---
id: "ts-packchk-m604"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M604: Currently no Dcore feature check for '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M604"
symptoms: ["M604", "Currently no Dcore feature check for '%NAME%'"]
symptom_regex: "^Currently no Dcore feature check for '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:239", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:481-540", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1284-1312", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/ProcessorFeatures/TestVendor.ProcessorFeatures.pdsc:65"]
---

## Symptom

`M604`
`Currently no Dcore feature check for '%NAME%'`

## Cause

A <processor> has a Dcore for which packchk keeps no list of required processor attributes (it knows Cortex-M0, M0+, M1, M3, M4, M7, M23, M33, M35P, M52, M55, M85, Star-MC1, SC000, SC300, ARMV8MBL, ARMV8MML and ARMV81MML), for example a Cortex-A or Cortex-R core or a misspelled Dcore. The attribute check (M605) is then skipped for that device.

## Fix

Nothing to change for a correctly spelled non-listed core; suppress with -x M604 if wanted. If the Dcore is misspelled, use the exact schema value, e.g. Dcore="Cortex-M33".

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:239`
- `tools/packchk/src/ValidateSemantic.cpp:481-540`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1284-1312`
- `tools/packchk/test/data/ProcessorFeatures/TestVendor.ProcessorFeatures.pdsc:65`
