---
id: "iss-pyocd-1486"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: reset_and_halt then resume logs 'cannot resume: target not halted'"
summary: "The message came from the automatic resume on disconnect, not from the resume call, so the script behaved correctly."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1486"
doc_source: "https://github.com/pyocd/pyOCD/issues/1486"
resolution: "not-a-bug"
versions: "0.34.3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The message came from the automatic resume on disconnect, not from the resume call, so the script behaved correctly.

## Fix

Pass resume_on_disconnect=False; the message was reworded in change #1487.

## Source

Resolution: not-a-bug

Versions: 0.34.3

From [pyocd/pyOCD #1486](https://github.com/pyocd/pyOCD/issues/1486), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
