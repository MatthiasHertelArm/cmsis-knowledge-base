---
id: "iss-rtx-34"
type: "troubleshooting"
domain: "rtos"
title: "RTX: osMutexRelease returns osErrorResource when called from another thread"
summary: "A mutex can only be released by its owner by definition."
status: "draft"
tool: "cmsis-rtx"
collection: "issues-rtx"
source: "https://github.com/ARM-software/CMSIS-RTX/issues/34"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/issues/34"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-rtx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A mutex can only be released by its owner by definition.

## Fix

Use a semaphore initialised with one token when different threads acquire and release.

## Source

Resolution: not-a-bug

From [ARM-software/CMSIS-RTX #34](https://github.com/ARM-software/CMSIS-RTX/issues/34), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
