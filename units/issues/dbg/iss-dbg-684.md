---
id: "iss-dbg-684"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD discovery stops with a critical error when a core AP has no pname in the pack"
summary: "A core access point discovered during CoreSight discovery (a hidden core) had no matching pname entry in the PDSC, and the mapping step raised instead of ignoring it."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/684"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/684"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["Microchip"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A core access point discovered during CoreSight discovery (a hidden core) had no matching pname entry in the PDSC, and the mapping step raised instead of ignoring it.

## Fix

Use a pyOCD with the fix (PR 1865, in develop since December 2025).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #684](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/684), summarized in own words; confidence high, not reviewed yet.
