---
id: "iss-pyocd-1826"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: LPC802 flash write gives partly written words with old pyOCD"
summary: "With pyOCD 0.34.3 the LPC802 reset-and-halt behaved differently from later versions, and a single word written to flash came out with only some bits set until the write was repeated."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1826"
doc_source: "https://github.com/pyocd/pyOCD/issues/1826"
resolution: "workaround"
versions: "Seen on 0.34.3; reported working from 0.36.0."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["LPC802"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With pyOCD 0.34.3 the LPC802 reset-and-halt behaved differently from later versions, and a single word written to flash came out with only some bits set until the write was repeated. A reporter reproduced it on 0.34.3 with both the Keil and NXP packs and found that 0.36.0 and later program the chip correctly, attributing it to the debug-sequence work in 0.35 and 0.36.

## Fix

Upgrade to pyOCD 0.36.0 or newer. If you must stay on 0.34.3, a user script with a will_reset/did_reset delegate that clears the reset vector catch and waits for the core to halt after reset worked around it. The original reporter had other chips fail on 0.36, so test your parts.

## Source

Resolution: workaround

Versions: Seen on 0.34.3; reported working from 0.36.0.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1826](https://github.com/pyocd/pyOCD/issues/1826), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
