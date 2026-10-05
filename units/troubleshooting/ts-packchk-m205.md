---
id: "ts-packchk-m205"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M205: Cannot create Pack Name file '…'"
status: "draft"
tool: "packchk"
severity: "error"
code: "M205"
symptoms: ["M205", "Cannot create Pack Name file '%PATH%'"]
symptom_regex: "^Cannot create Pack Name file '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:89", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk.cpp:54-84", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtefsutils/src/RteFsUtils.cpp:217-232", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:134"]
---

## Symptom

`M205`
`Cannot create Pack Name file '%PATH%'`

## Cause

Check the disk space or your permissions. Correct the path name.

## Fix

Give -n a path where packchk may write (it creates missing folders itself), e.g. -n build/packname.txt, and make sure the path is not an existing folder and the location is writable.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:89`
- `tools/packchk/src/PackChk.cpp:54-84`
- `libs/rtefsutils/src/RteFsUtils.cpp:217-232`
- `tools/packchk/README.md:134`
