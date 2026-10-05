---
id: "iss-pyocd-1276"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: -f frequency option ignored with ST-Link V3"
summary: "A copy-and-paste bug kept pyOCD from applying the requested SWD frequency to an ST-Link V3."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1276"
doc_source: "https://github.com/pyocd/pyOCD/issues/1276"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A copy-and-paste bug kept pyOCD from applying the requested SWD frequency to an ST-Link V3. After the fix the measured clock still differs from the request because of how the ST-Link V3 derives its frequencies, the same as in Keil MDK.

## Fix

Use a pyOCD with the fix, first available on the develop branch (pip install from git @develop); a new stlink.v3_prescaler option selects the probe's prescaler.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1276](https://github.com/pyocd/pyOCD/issues/1276), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
