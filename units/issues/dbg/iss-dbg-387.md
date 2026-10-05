---
id: "iss-dbg-387"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Symbol file paths in cbuild-run are relative to the file, which moved to the out folder"
summary: "Paths in the cbuild-run file are relative to that file, and pyOCD did not resolve them that way; this breaks once CMSIS-Toolbox 2.11 places the cbuild-run file in the out directory."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/387"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/387"
resolution: "workaround"
versions: "CMSIS-Toolbox 2.11 and later (2.10 not affected)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Paths in the cbuild-run file are relative to that file, and pyOCD did not resolve them that way; this breaks once CMSIS-Toolbox 2.11 places the cbuild-run file in the out directory.

## Fix

Use a pyOCD build with PR 1788 (validated with a local build together with a CMSIS-Toolbox nightly; no release named).

## Source

Resolution: workaround

Versions: CMSIS-Toolbox 2.11 and later (2.10 not affected)

From [Open-CMSIS-Pack/vscode-cmsis-debugger #387](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/387), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
