---
id: "iss-pyocd-1700"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32H7 flash corrupted occasionally with double buffering"
summary: "Double-buffered flash programming can stall on the bus of devices with strict timing such as STM32H7, leaving pages partly written (rest 0xFF) without any error."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1700"
doc_source: "https://github.com/pyocd/pyOCD/issues/1700"
resolution: "fixed-in-release"
versions: "fixed 0.37/0.38"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32H750VBTx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Double-buffered flash programming can stall on the bus of devices with strict timing such as STM32H7, leaving pages partly written (rest 0xFF) without any error.

## Fix

Upgrade to 0.37 or later, which disables double buffering by default; a built-in H743 target also worked better than the pack loader. Always verify flash after programming.

## Source

Resolution: fixed-in-release

Versions: fixed 0.37/0.38

From [pyocd/pyOCD #1700](https://github.com/pyocd/pyOCD/issues/1700), summarized in own words; confidence high, not reviewed yet.
