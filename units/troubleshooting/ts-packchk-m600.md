---
id: "ts-packchk-m600"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M600: Attribute '…' on '…' is deprecated."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M600"
symptoms: ["M600", "Attribute '%ATTR%' on '%TAG%' is deprecated."]
symptom_regex: "^Attribute '.+?' on '.+?' is deprecated\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints this warning when a PDSC file uses an attribute on an element that the CMSIS Pack schema has marked as deprecated."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M600`
`Attribute '%ATTR%' on '%TAG%' is deprecated.`

## Cause

packchk prints this warning when a PDSC file uses an attribute on an element that the CMSIS Pack schema has marked as deprecated. The %ATTR% placeholder is the attribute name and %TAG% is the element it appears on. The source lines were not available, so this reading comes from the message text alone.

## Fix

Find the element named in the message in the PDSC file and remove the deprecated attribute, or replace it with the current attribute that the CMSIS Pack specification recommends for that element. Then run packchk again to confirm the warning is gone.

## Note

The README does not document M600, and the trigger lines were not available to confirm the exact condition. The replacement attribute is not named here because the source does not show it. Verify the recommended replacement against the CMSIS Pack specification before applying it.
