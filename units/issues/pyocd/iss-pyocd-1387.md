---
id: "iss-pyocd-1387"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdbserver answers an unsupported qXfer request with a malformed '9+' reply"
summary: "pyOCD only handled target.xml for qXfer feature reads and returned a garbled packet for other files such as arm-m-profile.xml, leaving the client waiting."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1387"
doc_source: "https://github.com/pyocd/pyOCD/issues/1387"
resolution: "fixed-in-release"
versions: "0.31 to 0.33.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD only handled target.xml for qXfer feature reads and returned a garbled packet for other files such as arm-m-profile.xml, leaving the client waiting.

## Fix

Fixed by change #1414; update pyOCD.

## Source

Resolution: fixed-in-release

Versions: 0.31 to 0.33.1

From [pyocd/pyOCD #1387](https://github.com/pyocd/pyOCD/issues/1387), summarized in own words; confidence high, not reviewed yet.
