---
id: "iss-devtools-1147"
type: "troubleshooting"
domain: "project"
title: "cbuild: Path not found with backslashes in include path of a pack on macOS or Linux"
summary: "The pack's pdsc uses backslashes in file and include paths, which are not valid paths on macOS; packchk reports them as M327."
status: "draft"
tool: "cbuild"
symptoms: ["*** ERROR M204:\n  Path not found: '<packs>/GigaDevice/GD32F10x_DFP/2.0.3/Device\\Include'!"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1147"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1147"
resolution: "workaround"
versions: "toolbox 2.1.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "packchk"], "family": ["GD32F10x"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M204:
  Path not found: '<packs>/GigaDevice/GD32F10x_DFP/2.0.3/Device\Include'!`

## Cause

The pack's pdsc uses backslashes in file and include paths, which are not valid paths on macOS; packchk reports them as M327.

## Fix

Report it to the pack vendor, or edit the installed pdsc to use forward slashes (the reporter confirmed this works).

## Source

Resolution: workaround

Versions: toolbox 2.1.0

From [Open-CMSIS-Pack/devtools #1147](https://github.com/Open-CMSIS-Pack/devtools/issues/1147), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
