---
id: "ts-packchk-m602"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M602: Attribute '…' already set, see Line …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M602"
symptoms: ["M602", "Attribute '%ATTR%' already set, see Line %LINE%"]
symptom_regex: "^Attribute '.+?' already set, see Line .*$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "More than one <licenseSet> in <licenseSets> is marked default; only one license set can be the default."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:237", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:219-226", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:453-496", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/TestLicense/TestVendor.TestPackLicense.pdsc:17-24", "Open-CMSIS-Pack/devtools@30f5e817:libs/errlog/src/ErrLog.cpp:24-37"]
---

## Symptom

`M602`
`Attribute '%ATTR%' already set, see Line %LINE%`

## Cause

More than one <licenseSet> in <licenseSets> is marked default; only one license set can be the default. The message is logged without a line number, so its 'see Line' part is not filled in.

## Fix

Keep default="true" on exactly one <licenseSet> and remove it from the others.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:237`
- `tools/packchk/src/ValidateSyntax.cpp:219-226`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:453-496`
- `tools/packchk/test/data/TestLicense/TestVendor.TestPackLicense.pdsc:17-24`
- `libs/errlog/src/ErrLog.cpp:24-37`
