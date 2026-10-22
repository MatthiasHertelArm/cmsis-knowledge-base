---
id: "ts-packchk-m314"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M314: Filename '…' contains whitespaces, this is not recommended"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M314"
symptoms: ["M314", "Filename '%NAME%' contains whitespaces, this is not recommended"]
symptom_regex: "^Filename '.+?' contains whitespaces, this is not recommended$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "packchk prints M314 when a file name referenced by the pack, such as a source, header or documentation file listed in the PDSC, contains whitespace characters."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"]
---

## Symptom

`M314`
`Filename '%NAME%' contains whitespaces, this is not recommended`

## Cause

packchk prints M314 when a file name referenced by the pack, such as a source, header or documentation file listed in the PDSC, contains whitespace characters. The %NAME% in the message is the offending file name as written in the pack description. Whitespace in file names is flagged as not recommended, and the warning is emitted from the file-name check in packchk rather than from a build failure.

## Fix

Rename the file so its name has no spaces or other whitespace, for example replace spaces with underscores or hyphens, and update every reference to it in the PDSC (the url, name or path attributes that point to it). Then run packchk again to confirm the warning is gone.

## Note

Only the message text and the source file name were available; the trigger condition and the exact attribute checked were not read from the lines, so the cause is inferred from the message wording. The README does not document this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp`
