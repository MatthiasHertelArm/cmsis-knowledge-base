---
id: "ts-packchk-m605"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M605: Required Dcore '…' feature '…' not defined"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M605"
symptoms: ["M605", "Required Dcore '%NAME%' feature '%NAME2%' not defined"]
symptom_regex: "^Required Dcore '.+?' feature '.+?' not defined$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A <processor>, together with what it inherits from family and subFamily, lacks an attribute that packchk requires for its Dcore: Dfpu, Dmpu, Ddsp, Dendian, Dclock and DcoreVersion for every listed core; Dtz additionally for Cortex-M23, M33, M35P, M52, M55, …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:240", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:481-559", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1284-1312", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/ProcessorFeatures/TestVendor.ProcessorFeatures.pdsc:45-53"]
---

## Symptom

`M605`
`Required Dcore '%NAME%' feature '%NAME2%' not defined`

## Cause

A <processor>, together with what it inherits from family and subFamily, lacks an attribute that packchk requires for its Dcore: Dfpu, Dmpu, Ddsp, Dendian, Dclock and DcoreVersion for every listed core; Dtz additionally for Cortex-M23, M33, M35P, M52, M55, M85, Star-MC1, SC000, SC300 and the ARMV8M/ARMV81M cores; Dmve for M35P, M52, M55, M85, Star-MC1 and ARMV81MML. On devices with more than one processor every processor also needs Pname.

## Fix

Add the named attribute to the <processor> (or to the family or subFamily level it inherits from), e.g. <processor Dcore="Cortex-M4" DcoreVersion="r0p1" Dfpu="SP_FPU" Dmpu="MPU" Ddsp="DSP" Dendian="Little-endian" Dclock="100000000"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:240`
- `tools/packchk/src/ValidateSemantic.cpp:481-559`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1284-1312`
- `tools/packchk/test/data/ProcessorFeatures/TestVendor.ProcessorFeatures.pdsc:45-53`
