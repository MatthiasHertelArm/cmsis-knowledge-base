---
id: "iss-dbg-343"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd load prints a TypeError in load-svd and \"flash init timed out\""
summary: "The installed DFP version lacked the SVD file, so the SVD loader got None as path."
status: "draft"
tool: "pyocd"
symptoms: ["TypeError: expected str, bytes or os.PathLike object, not NoneType", "0005770 C flash init timed out [__main__]"]
symptom_regex: "TypeError:\\s+expected\\s+str,\\s+bytes\\s+or\\s+os\\.PathLike\\s+object,\\s+not\\s+NoneType"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/343"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/343"
resolution: "user-error"
versions: "CMSIS Debugger 0.3.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`TypeError: expected str, bytes or os.PathLike object, not NoneType`
`0005770 C flash init timed out [__main__]`

## Cause

The installed DFP version lacked the SVD file, so the SVD loader got None as path.

## Fix

Update the DFP to a version that ships the SVD; the cbuild-run file lists it under system-descriptions.

## Source

Resolution: user-error

Versions: CMSIS Debugger 0.3.1

From [Open-CMSIS-Pack/vscode-cmsis-debugger #343](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/343), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
