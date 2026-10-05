---
id: "ts-packchk-m389"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M389: that is resolved by the component itself."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M389"
symptoms: ["M389", "The component '%NAME%' (Line %LINE%) has dependency '%EXPR%' : '%NAME2%' that is resolved by the component itself."]
symptom_regex: "^The component '.+?' \\(Line .+?\\) has dependency '.+?' : '.+?' that is resolved by the component itself\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M389`
`The component '%NAME%' (Line %LINE%) has dependency '%EXPR%' : '%NAME2%' that is resolved by the component itself.`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_
