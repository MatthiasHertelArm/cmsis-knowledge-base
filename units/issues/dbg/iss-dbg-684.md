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
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["Microchip"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A core access point discovered during CoreSight discovery (a hidden core) had no matching pname entry in the PDSC, and the mapping step raised instead of ignoring it.

## Fix

Use a pyOCD build with PR 1865 (validated by the original reporter, merged into the develop branch; no release named). The earlier PR 1801 covered only the internal pack support, not cbuild-run targets.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #684](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/684), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
