---
id: "iss-pyocd-1276"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: -f frequency option ignored with ST-Link V3"
summary: "A copy and paste bug stopped the requested SWD frequency from being applied; the probe itself only produces certain frequencies."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1276"
doc_source: "https://github.com/pyocd/pyOCD/issues/1276"
resolution: "fixed-in-release"
versions: "0.32"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A copy and paste bug stopped the requested SWD frequency from being applied; the probe itself only produces certain frequencies.

## Fix

Fixed on the develop branch (later release); measured actual clock may differ from requested because of ST-Link V3 prescalers.

## Source

Resolution: fixed-in-release

Versions: 0.32

From [pyocd/pyOCD #1276](https://github.com/pyocd/pyOCD/issues/1276), summarized in own words; confidence medium, not reviewed yet.
