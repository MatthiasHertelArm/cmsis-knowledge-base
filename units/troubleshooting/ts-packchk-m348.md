---
id: "ts-packchk-m348"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M348: Feature redefined for '…', see Line …: '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M348"
symptoms: ["M348", "Feature redefined for '%MCU%', see Line %LINE%: '%PROP%'"]
symptom_regex: "^Feature redefined for '.+?', see Line .+?: '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "This feature _'FEATURE'_ has been defined already on the same level in line _'REF\\_LINE'_. The feature characteristics defined on line _'LINE'_ overwrite those from _'REF\\_LINE'_. Correct the feature ([/package/devices/family/.../feature](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_feature))."
summary: "Within one device-level element (family, subFamily, device or variant), two <feature> elements with the same type, m and name, or two <algorithm> elements with the same identity, apply to the same processor (same Pname, or both to all processors); …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:166", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:868-963", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1164-1201", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:794-824", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/DuplicateFlashAlgo/TestVendor.DuplicateFlashAlgo.pdsc:93-104", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:189"]
---

## Symptom

`M348`
`Feature redefined for '%MCU%', see Line %LINE%: '%PROP%'`

## Cause

Within one device-level element (family, subFamily, device or variant), two <feature> elements with the same type, m and name, or two <algorithm> elements with the same identity, apply to the same processor (same Pname, or both to all processors); a <board> can also list the same feature twice.

## Fix

Remove the duplicate entry, or make the two distinct (different Pname or attribute values) if both are meant.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:166`
- `tools/packchk/src/ValidateSyntax.cpp:868-963`
- `tools/packchk/src/ValidateSyntax.cpp:1164-1201`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:794-824`
- `tools/packchk/test/data/DuplicateFlashAlgo/TestVendor.DuplicateFlashAlgo.pdsc:93-104`
- `tools/packchk/README.md:189`
