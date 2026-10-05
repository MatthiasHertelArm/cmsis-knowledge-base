---
id: "iss-devtools-733"
type: "troubleshooting"
domain: "project"
title: "cbuild: IAR assembler error because the same define is passed globally and per file"
summary: "Defines add up through the hierarchy, so a define given both globally and for a single file appears twice on the command line, which the IAR assembler rejects."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/733"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/733"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Defines add up through the hierarchy, so a define given both globally and for a single file appears twice on the command line, which the IAR assembler rejects.

## Fix

Do not repeat a global define at file level. The thread points to CMSIS-Toolbox 1.5.0 for the fix without saying which change it contains.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #733](https://github.com/Open-CMSIS-Pack/devtools/issues/733), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
