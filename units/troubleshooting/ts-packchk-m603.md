---
id: "ts-packchk-m603"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M603: No license information found"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M603"
symptoms: ["M603", "No license information found"]
symptom_regex: "^No license information found$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The PDSC has neither a <license> element nor a <licenseSets> element with at least one <licenseSet>."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:238", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSyntax.cpp:182-258"]
---

## Symptom

`M603`
`No license information found`

## Cause

The PDSC has neither a <license> element nor a <licenseSets> element with at least one <licenseSet>.

## Fix

Ship the license text in the pack and reference it, e.g. <license>License.txt</license> under <package>, or <licenseSets><licenseSet id="all" default="true"><license name="License.txt" title="BSD-3-Clause"/></licenseSet></licenseSets>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:238`
- `tools/packchk/src/ValidateSyntax.cpp:182-258`
