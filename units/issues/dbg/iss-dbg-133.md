---
id: "iss-dbg-133"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Cannot read memory at peripheral register addresses with pyOCD"
summary: "pyOCD failed to read memory-mapped peripheral registers that the J-Link GDB server could read; the reporter suspected unmet memory-map requirements, and the thread does not confirm a cause."
status: "draft"
tool: "pyocd"
symptoms: ["Unable to read memory"]
symptom_regex: "Unable\\s+to\\s+read\\s+memory"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/133"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/133"
resolution: "fixed-in-release"
versions: "fixed in patch release 0.1.1 (with its pyOCD)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unable to read memory`

## Cause

pyOCD failed to read memory-mapped peripheral registers that the J-Link GDB server could read; the reporter suspected unmet memory-map requirements, and the thread does not confirm a cause.

## Fix

Use patch release 0.1.1 or later, whose pyOCD fixes these reads. The GDB command 'set mem inaccessible-by-default off' was only discussed as an additional option.

## Source

Resolution: fixed-in-release

Versions: fixed in patch release 0.1.1 (with its pyOCD)

From [Open-CMSIS-Pack/vscode-cmsis-debugger #133](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/133), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
