---
id: "iss-pyocd-1107"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Eclipse debug session: 'reset init' rejected by pyocd gdbserver"
summary: "An outdated Eclipse Embedded CDT pyOCD plugin sends the OpenOCD-style monitor command 'reset init', which pyocd does not accept as a reset type."
status: "draft"
tool: "pyocd"
symptoms: ["0005859:ERROR:gdbserver:Exception while executing remote command 'reset init': unexpected value for reset_type option ('init')"]
symptom_regex: "\\S+:ERROR:gdbserver:Exception\\s+while\\s+executing\\s+remote\\s+command\\s+'.*?':\\s+unexpected\\s+value\\s+for\\s+reset_type\\s+option\\s+\\('.*?'\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1107"
doc_source: "https://github.com/pyocd/pyOCD/issues/1107"
resolution: "configuration"
versions: "Embedded CDT before 6.1.1"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0005859:ERROR:gdbserver:Exception while executing remote command 'reset init': unexpected value for reset_type option ('init')`

## Cause

An outdated Eclipse Embedded CDT pyOCD plugin sends the OpenOCD-style monitor command 'reset init', which pyocd does not accept as a reset type.

## Fix

Update the Eclipse Embedded CDT plugins to 6.1.1 or later; this removed the error for the reporter.

## Source

Resolution: configuration

Versions: Embedded CDT before 6.1.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1107](https://github.com/pyocd/pyOCD/issues/1107), summarized in own words; confidence high, not reviewed yet.
