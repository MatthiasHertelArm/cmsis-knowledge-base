---
id: "iss-pyocd-1794"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd commander exits 0 when no matching debug probe is found"
summary: "When the requested probe cannot be found, pyocd commander prints the error but still exits with status 0 instead of a non-zero code, so scripts that rely on the exit code cannot detect the failure."
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
applies_to: {"tool": ["pyocd"], "component": ["commander"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No connected debug probe matches unique ID '12345'`

## Cause

When the requested probe cannot be found, pyocd commander prints the error but still exits with status 0 instead of a non-zero code, so scripts that rely on the exit code cannot detect the failure.

## Fix

The thread points to #2037 as the intended fix; the issue is still open and the thread does not say whether it is merged or released.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1794](https://github.com/pyocd/pyOCD/issues/1794), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
