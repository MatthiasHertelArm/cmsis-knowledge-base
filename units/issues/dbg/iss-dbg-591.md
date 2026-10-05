---
id: "iss-dbg-591"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: Debug Console flooded by \"Failed to decode cstring\" while RTOS Views is open"
summary: "The CDT GDB Adapter failed to decode non-UTF-8 bytes in strings read by the RTOS view and logged each one."
status: "draft"
tool: "cmsis-debugger"
symptoms: ["Failed to decode cstring '241 'ñ''. {}"]
symptom_regex: "Failed\\s+to\\s+decode\\s+cstring\\s+'.*?'ñ'.*?'\\.\\s+\\{\\}"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/591"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/591"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-debugger"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Failed to decode cstring '241 'ñ''. {}`

## Cause

The CDT GDB Adapter failed to decode non-UTF-8 bytes in strings read by the RTOS view and logged each one.

## Fix

Update CDT GDB Adapter to 2.5.0 or later.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #591](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/591), summarized in own words; confidence medium, not reviewed yet.
