---
id: "ts-packchk-m213"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M213: Found blank char '…' in Packname output filename, deleted"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M213"
symptoms: ["M213", "Found blank char '%NUM%' in Packname output filename, deleted"]
symptom_regex: "^Found blank char '.+?' in Packname output filename, deleted$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "The file name given with option -n (text file that receives the pack name) contains a space, tab, carriage return or line feed. packchk deletes each such character from the whole path, folder names included, and prints its decimal …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:99", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackOptions.cpp:57-74", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk.cpp:138-157", "Open-CMSIS-Pack/devtools@30f5e817:libs/errlog/include/ErrLog.h:66"]
---

## Symptom

`M213`
`Found blank char '%NUM%' in Packname output filename, deleted`

## Cause

The file name given with option -n (text file that receives the pack name) contains a space, tab, carriage return or line feed. packchk deletes each such character from the whole path, folder names included, and prints its decimal character code (32 is a space), so the file is written to a different path than the one given.

## Fix

Give -n a path without blanks, e.g. -n out/packname.txt, so the pack name file lands where the build script expects it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:99`
- `tools/packchk/src/PackOptions.cpp:57-74`
- `tools/packchk/src/PackChk.cpp:138-157`
- `libs/errlog/include/ErrLog.h:66`
