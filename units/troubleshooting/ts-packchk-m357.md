---
id: "ts-packchk-m357"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M357: Config File '…', which gets copied to project, is also found in the include path to the original …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M357"
symptoms: ["M357", "Config File '%NAME%', which gets copied to project, is also found in the include path to the original pack folder. Do not place config header files in the same directory as regular header files. See Line %LINE%"]
symptom_regex: "^Config File '.+?', which gets copied to project, is also found in the include path to the original pack folder\\. Do not place config header files in the same directory as regular header files\\. See Line .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints M357 when a file named in the pack's config-file list (a header that the pack asks to be copied into the user project) is also reachable through the include path pointing into the original pack folder."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M357`
`Config File '%NAME%', which gets copied to project, is also found in the include path to the original pack folder. Do not place config header files in the same directory as regular header files. See Line %LINE%`

## Cause

packchk prints M357 when a file named in the pack's config-file list (a header that the pack asks to be copied into the user project) is also reachable through the include path pointing into the original pack folder. The %NAME% is the config file name and %LINE% is the line of the offending reference. The clash means the same header name exists both as a project-copied config file and as a regular header in the pack's include directory, so the compiler could pick either copy.

## Fix

Move the config header (the file that the PDSC marks as a config file to be copied) out of the directory that holds the regular pack headers, so that the include directory no longer contains it, then update the PDSC path and the include path accordingly. Keep config headers and regular headers in separate directories.

## Note

Written without the source lines (clone not available), so the trigger condition and the exact fix are inferred from the message text only. The README does not document this message. Verify the trigger in tools/packchk/src/PackChk_Msgs.cpp before relying on the fix wording.
