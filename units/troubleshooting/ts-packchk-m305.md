---
id: "ts-packchk-m305"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M305: No releases (\"<release>\" elements in a <releases>-tag) found in PDSC file!"
status: "draft"
tool: "packchk"
severity: "error"
code: "M305"
symptoms: ["M305", "No releases (\"<release>\" elements in a <releases>-tag) found in PDSC file!"]
symptom_regex: "^No releases \\(\"<release>\" elements in a <releases>\\-tag\\) found in PDSC file!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "At least one package release shall be specified in the PDSC file, but none was not found. Use `<release>` tag to specify release information in `<releases>` element. Refer to [/package/releases/release](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html#element_release)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:117", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:291-302", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:154"]
---

## Symptom

`M305`
`No releases ("<release>" elements in a <releases>-tag) found in PDSC file!`

## Cause

The PDSC has a <releases> element, but it contains no <release>.

## Fix

Add at least one release, newest first: <releases><release version="1.0.0" date="2026-01-31">Initial release</release></releases>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:117`
- `tools/packchk/src/ValidateSyntax.cpp:291-302`
- `tools/packchk/README.md:154`
