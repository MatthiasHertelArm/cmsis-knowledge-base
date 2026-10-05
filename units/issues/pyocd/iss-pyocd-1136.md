---
id: "iss-pyocd-1136"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing a blank LPC5526 fails with a memory transfer fault"
summary: "LPC5526 had no built-in target in pyOCD and fell back to generic handling, which cannot program the blank part the way the LPC55xx family code does; erase alone worked."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1136"
doc_source: "https://github.com/pyocd/pyOCD/issues/1136"
resolution: "fixed-in-release"
versions: "seen with 0.30.3"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC5526"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

LPC5526 had no built-in target in pyOCD and fell back to generic handling, which cannot program the blank part the way the LPC55xx family code does; erase alone worked. The reporter noticed the LPC5500 family code carried a note about this.

## Fix

Add a built-in target for the LPC5526 based on the LPC5500 family class (the reporter did this and could flash, erase and debug). Use a pyOCD release that includes the LPC5526 target.

## Source

Resolution: fixed-in-release

Versions: seen with 0.30.3

From [pyocd/pyOCD #1136](https://github.com/pyocd/pyOCD/issues/1136), summarized in own words; confidence medium, not reviewed yet.
