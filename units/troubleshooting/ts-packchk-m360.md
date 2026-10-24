---
id: "ts-packchk-m360"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M360: Subfamily has no Device(s): '…"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M360"
symptoms: ["M360", "Subfamily has no Device(s): '%SUBFAMILY%"]
symptom_regex: "^Subfamily has no Device\\(s\\): '.*$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Add the missing information. Refer to [/package/devices/family/subFamily](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_subFamily)."
summary: "A <subFamily> element contains no <device> element."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:179", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:1337-1347", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:199"]
---

## Symptom

`M360`
`Subfamily has no Device(s): '%SUBFAMILY%`

## Cause

A <subFamily> element contains no <device> element.

## Fix

Add <device> elements to the subFamily, or remove it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:179`
- `tools/packchk/src/ValidateSyntax.cpp:1337-1347`
- `tools/packchk/README.md:199`
