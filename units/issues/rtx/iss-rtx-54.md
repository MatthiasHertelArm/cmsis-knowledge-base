---
id: "iss-rtx-54"
type: "troubleshooting"
domain: "rtos"
title: "RTX: osMessageQueueNew fails with user control block that is larger than required"
summary: "RTX with safety features checks that cb_size equals the control block size exactly, contrary to CMSIS 5 text calling it a minimum."
status: "draft"
tool: "cmsis-rtx"
collection: "issues-rtx"
source: "https://github.com/ARM-software/CMSIS-RTX/issues/54"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/issues/54"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-rtx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

RTX with safety features checks that cb_size equals the control block size exactly, contrary to CMSIS 5 text calling it a minimum.

## Fix

Pass exactly osRtxMessageQueueCbSize as cb_size.

## Source

Resolution: not-a-bug

From [ARM-software/CMSIS-RTX #54](https://github.com/ARM-software/CMSIS-RTX/issues/54), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
