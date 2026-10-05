---
id: "iss-pyocd-1842"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd load fails on boards without nRESET wired (3-wire SWD) since 0.40"
summary: "From 0.40.0 the load command always performs a hardware reset via nSRST afterwards, which does nothing useful or breaks SWD when the reset pin is not connected."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1842"
doc_source: "https://github.com/pyocd/pyOCD/issues/1842"
resolution: "fixed-in-release"
versions: "broken 0.40.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

From 0.40.0 the load command always performs a hardware reset via nSRST afterwards, which does nothing useful or breaks SWD when the reset pin is not connected.

## Fix

Workaround: 'pyocd load --no-reset ...' followed by 'pyocd reset'. The fixed releases add pre-reset and post-reset session options and restore the old default behaviour.

## Source

Resolution: fixed-in-release

Versions: broken 0.40.0

From [pyocd/pyOCD #1842](https://github.com/pyocd/pyOCD/issues/1842), summarized in own words; confidence high, not reviewed yet.
