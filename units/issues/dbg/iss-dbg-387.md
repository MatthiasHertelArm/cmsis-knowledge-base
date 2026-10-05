---
id: "iss-dbg-387"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Symbol file paths in cbuild-run are relative to the file, which moved to the out folder"
summary: "pyOCD resolved relative paths against the working directory; with CMSIS-Toolbox 2.11 the cbuild-run file sits in out."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/387"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/387"
resolution: "fixed-in-release"
versions: "CMSIS-Toolbox 2.11 and later"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD resolved relative paths against the working directory; with CMSIS-Toolbox 2.11 the cbuild-run file sits in out.

## Fix

Use pyOCD with PR 1788 (paths resolved relative to the cbuild-run file location).

## Source

Resolution: fixed-in-release

Versions: CMSIS-Toolbox 2.11 and later

From [Open-CMSIS-Pack/vscode-cmsis-debugger #387](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/387), summarized in own words; confidence high, not reviewed yet.
