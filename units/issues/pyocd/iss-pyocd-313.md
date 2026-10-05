---
id: "iss-pyocd-313"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver AssertionError at start because another program holds the probe"
summary: "pyOCD's pywinusb backend timed out opening the probe and hit an assert, which the maintainers read as another process (not pyOCD, which opens the probe exclusively) holding the board."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception:", "AssertionError"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/313"
doc_source: "https://github.com/pyocd/pyOCD/issues/313"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception:`
`AssertionError`

## Cause

pyOCD's pywinusb backend timed out opening the probe and hit an assert, which the maintainers read as another process (not pyOCD, which opens the probe exclusively) holding the board.

## Fix

Not confirmed in the thread: find and close the other program that has the board open, then start pyocd-gdbserver again.

## Source

Resolution: user-error

From [pyocd/pyOCD #313](https://github.com/pyocd/pyOCD/issues/313), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
