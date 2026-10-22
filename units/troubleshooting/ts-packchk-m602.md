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
symptom_regex: "^Attribute '.+?' already set, see Line .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "unknown"
---

## Symptom

`M602`
`Attribute '%ATTR%' already set, see Line %LINE%`

## Cause

_open: to be written in the review_

## Fix

_open: to be written in the review_

## Note

The source clone was not available and no trigger lines were given, so only the message text can be read: an attribute named by %ATTR% was already set earlier on the same element, at the line given by %LINE%. A likely reading is a duplicate XML attribute in a pack description file, but the source does not confirm the element type or the trigger condition. Verify the trigger in tools/packchk/src/PackChk_Msgs.cpp before writing a cause and fix. The README does not document this message.
