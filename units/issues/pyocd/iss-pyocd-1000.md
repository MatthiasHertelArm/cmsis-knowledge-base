---
id: "iss-pyocd-1000"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb drops pyocd gdbserver connection: 'Reply contains invalid hex digit 120'"
summary: "The core was not halted when gdb connected (here a watchdog reset the target after pyocd halted it)."
status: "draft"
tool: "pyocd"
symptoms: ["Reply contains invalid hex digit 120"]
symptom_regex: "Reply\\s+contains\\s+invalid\\s+hex\\s+digit\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1000"
doc_source: "https://github.com/pyocd/pyOCD/issues/1000"
resolution: "workaround"
versions: "pyOCD dev builds late 2020; seen on SAM4L and nRF5340"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd", "gdb"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Reply contains invalid hex digit 120`

## Cause

The core was not halted when gdb connected (here a watchdog reset the target after pyocd halted it). Register reads then fail and pyocd returns 'xxxxxxxx' as unavailable values in the first stop reply, which gdb cannot parse as hex.

## Fix

Make sure the core is halted when gdb attaches: disable or freeze the watchdog while debugging (for example the debug-halt option of the watchdog), then restart pyocd gdbserver.

## Source

Resolution: workaround

Versions: pyOCD dev builds late 2020; seen on SAM4L and nRF5340

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1000](https://github.com/pyocd/pyOCD/issues/1000), summarized in own words; confidence medium, not reviewed yet.
