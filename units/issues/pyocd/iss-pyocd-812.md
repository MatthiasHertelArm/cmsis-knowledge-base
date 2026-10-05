---
id: "iss-pyocd-812"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: NUCLEO-H743ZI2 flash fails with STLink error (5) No device connected"
summary: "The ST-Link loses the target after the first AP ID read, suggesting the STM32H7 goes to sleep or the debug domain is not awake."
status: "draft"
tool: "pyocd"
symptoms: ["STLink error (5): No device connected"]
symptom_regex: "STLink\\s+error\\s+\\(\\S+\\):\\s+No\\s+device\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/812"
doc_source: "https://github.com/pyocd/pyOCD/issues/812"
resolution: "workaround"
versions: "0.24.1 and 0.25.0"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["STM32H7 Series"], "device": ["STM32H743ZITx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`STLink error (5): No device connected`

## Cause

The ST-Link loses the target after the first AP ID read, suggesting the STM32H7 goes to sleep or the debug domain is not awake.

## Fix

Retry with -Oconnect_mode=under-reset; one participant reported this solved it, another reported it still failed, so also use a DBGMCU_CR user script or a non-sleeping build.

## Source

Resolution: workaround

Versions: 0.24.1 and 0.25.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #812](https://github.com/pyocd/pyOCD/issues/812), summarized in own words; confidence low, not reviewed yet.
