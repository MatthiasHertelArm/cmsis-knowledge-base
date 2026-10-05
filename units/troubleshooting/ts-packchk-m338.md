---
id: "ts-packchk-m338"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M338: No releases found!"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M338"
symptoms: ["M338", "No releases found!"]
symptom_regex: "^No releases found!$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "The PDSC file is missing release information. Add `<release>` information to the file. Refer to [/package/releases element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html)."
summary: "The PDSC has no <releases> element at all. packchk then also skips the package description and PDSC file name checks."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:156", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:291-296", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:179"]
---

## Symptom

`M338`
`No releases found!`

## Cause

The PDSC has no <releases> element at all. packchk then also skips the package description and PDSC file name checks.

## Fix

Add <releases> under <package> with at least one release, newest first: <releases><release version="1.0.0" date="2026-01-31">Initial release</release></releases>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:156`
- `tools/packchk/src/ValidateSyntax.cpp:291-296`
- `tools/packchk/README.md:179`
