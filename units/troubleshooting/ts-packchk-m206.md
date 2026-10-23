---
id: "ts-packchk-m206"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M206: Multiple PDSC file found in package: …"
status: "draft"
tool: "packchk"
severity: "error"
code: "M206"
symptoms: ["M206", "Multiple PDSC file found in package: %FILES%"]
symptom_regex: "^Multiple PDSC file found in package: .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Only one PDSC file is allowed in a package. Remove unnecessary PDSC files. The message lists all \\*.pdsc files found."
summary: "The folder that contains the PDSC holds more than one *.pdsc file; only that folder is searched, not its subfolders."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:90", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CreateModel.cpp:39-86", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtefsutils/src/RteFsUtils.cpp:750-788", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ParseOptions.cpp:222", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:135"]
---

## Symptom

`M206`
`Multiple PDSC file found in package: %FILES%`

## Cause

The folder that contains the PDSC holds more than one *.pdsc file; only that folder is searched, not its subfolders. A pack may contain only one PDSC.

## Fix

Delete the other .pdsc files from the pack root or move them out of the pack, or run with --ignore-other-pdsc if they must stay.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:90`
- `tools/packchk/src/CreateModel.cpp:39-86`
- `libs/rtefsutils/src/RteFsUtils.cpp:750-788`
- `tools/packchk/src/ParseOptions.cpp:222`
- `tools/packchk/README.md:135`
