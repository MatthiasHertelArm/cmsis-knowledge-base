---
id: "iss-pyocd-1794"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd commander exits with status 0 when no probe matches the unique ID"
summary: "When the requested debug probe cannot be found, commander prints an error message but still exits with status zero, so the return code does not reveal the failure."
status: "draft"
tool: "pyocd"
symptoms: ["No connected debug probe matches unique ID '12345'"]
symptom_regex: "No\\s+connected\\s+debug\\s+probe\\s+matches\\s+unique\\s+ID\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1794"
doc_source: "https://github.com/pyocd/pyOCD/issues/1794"
resolution: "unresolved"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No connected debug probe matches unique ID '12345'`

## Cause

When the requested debug probe cannot be found, commander prints an error message but still exits with status zero, so the return code does not reveal the failure.

## Fix

The thread points to PR #2037 as the fix; it gives no workaround and does not confirm the PR is merged.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1794](https://github.com/pyocd/pyOCD/issues/1794), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
