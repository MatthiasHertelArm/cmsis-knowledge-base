---
id: "iss-pyocd-1049"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Device pack not found by 'pyocd pack --install' although it worked before"
summary: "The local pack index cache was stale or missing the entry."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1049"
doc_source: "https://github.com/pyocd/pyOCD/issues/1049"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["ATSAML21J18A"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The local pack index cache was stale or missing the entry.

## Fix

Run `pyocd pack -c` to clear the cache and `pyocd pack -u` to update the index, then install again.

## Source

Resolution: workaround

From [pyocd/pyOCD #1049](https://github.com/pyocd/pyOCD/issues/1049), summarized in own words; confidence medium, not reviewed yet.
