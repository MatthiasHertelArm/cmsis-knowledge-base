---
id: "ts-packchk-m301"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M301: Checking Pack URL of PDSC file failed: Expected URL : '…' Package URL : '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M301"
symptoms: ["M301", "Checking Pack URL of PDSC file failed:   Expected URL : '%URL1%'   Package  URL : '%URL2%'"]
symptom_regex: "^Checking Pack URL of PDSC file failed:$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The URL specified in the package does not match the value entered for comparison in option `-u`."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:109-111", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:502-540", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackOptions.cpp:294-316", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:263-279", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:150"]
---

## Symptom

`M301`
`Checking Pack URL of PDSC file failed:   Expected URL : '%URL1%'   Package  URL : '%URL2%'`

## Cause

The URL specified in the package does not match the value entered for comparison in option `-u`. Check for possible misspellings in both URLs. Refer to [/package/url](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_package_pg.html#package_url).

## Fix

Make <url> start with the URL given to -u (compared without regard to case; trailing slashes of the -u value are ignored), or correct the -u value, e.g. -u https://www.myvendor.com/pack/ with <url>https://www.myvendor.com/pack/</url>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:109-111`
- `tools/packchk/src/ValidateSyntax.cpp:502-540`
- `tools/packchk/src/PackOptions.cpp:294-316`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:263-279`
- `tools/packchk/README.md:150`
