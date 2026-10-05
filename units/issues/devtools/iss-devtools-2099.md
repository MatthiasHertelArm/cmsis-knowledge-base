---
id: "iss-devtools-2099"
type: "troubleshooting"
domain: "project"
title: "csolution: pyOCD launch error because cbuild-run.yml has a dbgconf node the device does not define"
summary: "csolution wrote dbgconf: into cbuild-run.yml even when the pack's debugvars element has no configfile attribute, so the debugger tried to use a file that does not exist."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2099"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2099"
resolution: "fixed-in-release"
versions: "2.9.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution", "pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution wrote dbgconf: into cbuild-run.yml even when the pack's debugvars element has no configfile attribute, so the debugger tried to use a file that does not exist.

## Fix

Fixed in toolbox builds after 2.9.0; the dbgconf node is only written when the pack specifies a configfile.

## Source

Resolution: fixed-in-release

Versions: 2.9.0

From [Open-CMSIS-Pack/devtools #2099](https://github.com/Open-CMSIS-Pack/devtools/issues/2099), summarized in own words; confidence high, not reviewed yet.
