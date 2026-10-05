---
id: "ts-packchk-m357"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M357: , which gets copied to project, is also found in the include path to t"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M357"
symptoms: ["M357", "Config File '%NAME%', which gets copied to project, is also found in the include path to the original pack folder. Do not place config header files in the same directory as regular header files. See Line %LINE%"]
symptom_regex: "^Config File '.+?', which gets copied to project, is also found in the include path to the original pack folder\\. Do not place config header files in the same directory as regular header files\\. See Line .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e81:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
---

## Symptom

`M357`
`Config File '%NAME%', which gets copied to project, is also found in the include path to the original pack folder. Do not place config header files in the same directory as regular header files. See Line %LINE%`

## Cause

_offen, im Review ergänzen_

## Fix

_offen, im Review ergänzen_
