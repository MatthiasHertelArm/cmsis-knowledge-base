---
id: "ts-packchk-m367"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M367: Redefined … '…' found, see Line …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M367"
symptoms: ["M367", "Redefined %TYPE% '%NAME%' found, see Line %LINE%"]
symptom_regex: "^Redefined .+? '.+?' found, see Line .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Remove duplicate device/variant entries. Refer to [/package/devices/family/../device](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_device)."
summary: "Two sibling elements have the same name: for example two <device> elements with the same Dname in one family or subFamily, or two <licenseSet> elements with the same id. %TYPE% says which kind (Family, Subfamily, Device, Variant or id)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:186", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1354-1364", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:208-214", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:453-496", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/TestLicense/TestVendor.TestPackLicense.pdsc:21-24", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:206"]
---

## Symptom

`M367`
`Redefined %TYPE% '%NAME%' found, see Line %LINE%`

## Cause

Two sibling elements have the same name: for example two <device> elements with the same Dname in one family or subFamily, or two <licenseSet> elements with the same id. %TYPE% says which kind (Family, Subfamily, Device, Variant or id).

## Fix

Rename or remove the duplicate element.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:186`
- `tools/packchk/src/ValidateSyntax.cpp:1354-1364`
- `tools/packchk/src/ValidateSyntax.cpp:208-214`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:453-496`
- `tools/packchk/test/data/TestLicense/TestVendor.TestPackLicense.pdsc:21-24`
- `tools/packchk/README.md:206`
