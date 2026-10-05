---
id: "iss-cmsis6-287"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: GCC linker script template shows RAM usage 100 percent"
summary: "The stack section in the template is placed at the end of RAM and counted as used by the linker report; the layout is intended."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/287"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/287"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-core"], "toolchain": ["GCC"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The stack section in the template is placed at the end of RAM and counted as used by the linker report; the layout is intended.

## Fix

Accept the figure or make the stack NOLOAD, which loses the stack at the end of RAM and risks overflows into heap.

## Source

Resolution: not-a-bug

From [ARM-software/CMSIS_6 #287](https://github.com/ARM-software/CMSIS_6/issues/287), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
