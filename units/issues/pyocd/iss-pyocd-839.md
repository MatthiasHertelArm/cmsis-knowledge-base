---
id: "iss-pyocd-839"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: i.MX RT1010 EVK is reported as an RT1050 EVK in pyocd list"
summary: "Early OpenSDA firmware for the RT1010 EVK still carried the RT1050 board ID in the unique ID."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/839"
doc_source: "https://github.com/pyocd/pyOCD/issues/839"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Early OpenSDA firmware for the RT1010 EVK still carried the RT1050 board ID in the unique ID.

## Fix

Update the board's debug firmware to a current release.

## Source

Resolution: configuration

From [pyocd/pyOCD #839](https://github.com/pyocd/pyOCD/issues/839), summarized in own words; confidence high, checked against the thread, not reviewed yet.
