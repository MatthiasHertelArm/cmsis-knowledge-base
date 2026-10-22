---
id: "iss-dbg-1170"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Trace source disabled during debug session keeps producing packets (SWO exception trace)"
summary: "Trace setup is generated only for features that are enabled, so a feature switched off in the session emits no register write that could clear its enable bit. pyOCD then programs registers by read-modify-write from the enabled features only, …"
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1170"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1170"
resolution: "fixed-in-release"
versions: "Tested with pyocd 0.45.2.dev39+ga3e58b2b5 in CMSIS Debugger Nightly 1.8.1-78-g8c7d39f"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Trace setup is generated only for features that are enabled, so a feature switched off in the session emits no register write that could clear its enable bit. pyOCD then programs registers by read-modify-write from the enabled features only, so the previously set bits stay on in the target.

## Fix

The trace specification was extended so that cleared or reset register states for disabled features are also sent to pyOCD, which applies them. pyTS and pyOCD were updated to support this. Tested with pyocd 0.45.2.dev39+ga3e58b2b5 in CMSIS Debugger Nightly 1.8.1-78-g8c7d39f, where disabled trace features such as exception trace were reported to work as expected.

## Source

Resolution: fixed-in-release

Versions: Tested with pyocd 0.45.2.dev39+ga3e58b2b5 in CMSIS Debugger Nightly 1.8.1-78-g8c7d39f

From [Open-CMSIS-Pack/vscode-cmsis-debugger #1170](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/1170), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
