---
id: "ts-packchk-m601"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M601: '…' missing on '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M601"
symptoms: ["M601", "'%TAG%' missing on '%TAG2%'"]
symptom_regex: "^'.+?' missing on '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:236", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:191-245", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckFiles.cpp:993-1059", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:453-496", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/TestLicense/TestVendor.TestPackLicense.pdsc:27-28", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/CsolutionTag/TestVendor.CsolutionTag.pdsc:37-54"]
---

## Symptom

`M601`
`'%TAG%' missing on '%TAG2%'`

## Cause

A required part is missing: <licenseSets> without any <licenseSet>; a <licenseSet> without <license>; a <license> without name or title; in <csolution>, a <clayer> without type, path or file, or a <template> without name, path, file or a <description> child. %TAG% is what is missing, %TAG2% the element that lacks it.

## Fix

Add what the message names, e.g. <license name="licenses/MIT.txt" title="MIT License"/>, or <clayer type="Board" path="boards/myboard/layers" file="Board.clayer.yml"/>.

## Note

<csolution>, <clayer> and <template> are not in the 1.7.15 schema copy in the tree (tools/packchk/test/data/schema.xsd); PACK.xsd itself is not in the tree, so these names come from CheckFiles.cpp and the test pack.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:236`
- `tools/packchk/src/ValidateSyntax.cpp:191-245`
- `tools/packchk/src/CheckFiles.cpp:993-1059`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:453-496`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1201-1247`
- `tools/packchk/test/data/TestLicense/TestVendor.TestPackLicense.pdsc:27-28`
- `tools/packchk/test/data/CsolutionTag/TestVendor.CsolutionTag.pdsc:37-54`
