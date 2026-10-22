---
id: "ts-packchk-m308"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M308: Attribute '…' missing on '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M308"
symptoms: ["M308", "Attribute '%TAG%' missing on '%TAG2%'"]
symptom_regex: "^Attribute '.+?' missing on '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Element _'TAG2'_ requires attribute _'TAG'_, but it was not found. Add missing attribute."
summary: "An element lacks an attribute packchk requires: a <memory> without start or size, a <mountedDevice> without Dvendor or Dname, or a <licenseSet> without id."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:122", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:259-265", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1713-1721", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:203-206", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1133-1172", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:91-92", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:157"]
---

## Symptom

`M308`
`Attribute '%TAG%' missing on '%TAG2%'`

## Cause

An element lacks an attribute packchk requires: a <memory> without start or size, a <mountedDevice> without Dvendor or Dname, or a <licenseSet> without id.

## Fix

Add the attribute named in the message to that element, e.g. <memory name="SRAM" access="rw" start="0x20000000" size="0x00010000"/> or <mountedDevice deviceIndex="0" Dvendor="ARM:82" Dname="ARMCM4"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:122`
- `tools/packchk/src/ValidateSemantic.cpp:259-265`
- `tools/packchk/src/ValidateSyntax.cpp:1713-1721`
- `tools/packchk/src/ValidateSyntax.cpp:203-206`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1133-1172`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:989-1036`
- `tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:91-92`
- `tools/packchk/README.md:157`
