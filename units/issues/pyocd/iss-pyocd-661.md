---
id: "iss-pyocd-661"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Nucleo-L476RG 'STLink error (9): Get IDCODE error' after removing CN2 jumpers"
summary: "With both CN2 jumpers off, the on-board ST-LINK is routed to the external CN4 header and no longer talks to the on-board STM32 target."
status: "draft"
tool: "pyocd"
symptoms: ["0001855:ERROR:__main__:uncaught exception: STLink error (9): Get IDCODE error"]
symptom_regex: "\\S+:ERROR:__main__:uncaught\\s+exception:\\s+STLink\\s+error\\s+\\(\\S+\\):\\s+Get\\s+IDCODE\\s+error"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/661"
doc_source: "https://github.com/pyocd/pyOCD/issues/661"
resolution: "user-error"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["STM32L476RGTx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001855:ERROR:__main__:uncaught exception: STLink error (9): Get IDCODE error`

## Cause

With both CN2 jumpers off, the on-board ST-LINK is routed to the external CN4 header and no longer talks to the on-board STM32 target.

## Fix

Put the CN2 jumpers back on to program the on-board MCU. Leave them off only to debug an external target through CN4.

## Source

Resolution: user-error

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #661](https://github.com/pyocd/pyOCD/issues/661), summarized in own words; confidence high, checked against the thread, not reviewed yet.
