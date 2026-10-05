---
id: "iss-pyocd-1264"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: enable_semihosting option in pyocd.yaml or -O is ignored"
summary: "The -S/--semihosting command line flag always overrides the initial value of the enable_semihosting option from -O or config, even if the flag is not given."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1264"
doc_source: "https://github.com/pyocd/pyOCD/issues/1264"
resolution: "workaround"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The -S/--semihosting command line flag always overrides the initial value of the enable_semihosting option from -O or config, even if the flag is not given.

## Fix

Pass --semihosting on the pyocd gdbserver command line, or enable it at runtime with monitor arm semihosting enable.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1264](https://github.com/pyocd/pyOCD/issues/1264), summarized in own words; confidence high, not reviewed yet.
