---
id: "iss-pyocd-1794"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd commander returns exit code 0 when no matching debug probe is found"
summary: "When pyocd commander cannot find the probe given by unique ID, it prints the error but exits with status 0 instead of a non-zero code, so scripts that check the return code see success."
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
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No connected debug probe matches unique ID '12345'`

## Cause

When pyocd commander cannot find the probe given by unique ID, it prints the error but exits with status 0 instead of a non-zero code, so scripts that check the return code see success.

## Fix

A maintainer says the problem should be fixed with PR #2037; the issue is still open and the thread gives no interim workaround.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1794](https://github.com/pyocd/pyOCD/issues/1794), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
