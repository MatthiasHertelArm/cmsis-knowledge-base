---
id: "iss-pyocd-1136"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing a blank LPC5526 fails with a memory transfer fault"
summary: "LPC5526 had no built-in pyOCD target, unlike the LPC55S28 whose target uses the LPC5500 family code (which carries a comment the reporter suspected matches this case); flashing a blank part failed with a memory transfer fault while erase always worked."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1136"
doc_source: "https://github.com/pyocd/pyOCD/issues/1136"
resolution: "workaround"
versions: "0.30.3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["LPC5526"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

LPC5526 had no built-in pyOCD target, unlike the LPC55S28 whose target uses the LPC5500 family code (which carries a comment the reporter suspected matches this case); flashing a blank part failed with a memory transfer fault while erase always worked.

## Fix

Add a built-in target for the LPC5526 like the LPC55S28 one; the reporter did this and could then flash, erase and debug.

## Source

Resolution: workaround

Versions: 0.30.3

From [pyocd/pyOCD #1136](https://github.com/pyocd/pyOCD/issues/1136), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
