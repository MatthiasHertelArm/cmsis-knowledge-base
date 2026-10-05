---
id: "iss-pyocd-1091"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: The -O option for the SWV clock seems to be ignored"
summary: "The option name was misspelled as smv_clock; the real option is swv_clock, and unknown names are silently ignored."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1091"
doc_source: "https://github.com/pyocd/pyOCD/issues/1091"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The option name was misspelled as smv_clock; the real option is swv_clock, and unknown names are silently ignored.

## Fix

Pass `-O swv_clock=<hz>` with the correct spelling.

## Source

Resolution: user-error

From [pyocd/pyOCD #1091](https://github.com/pyocd/pyOCD/issues/1091), summarized in own words; confidence high, checked against the thread, not reviewed yet.
