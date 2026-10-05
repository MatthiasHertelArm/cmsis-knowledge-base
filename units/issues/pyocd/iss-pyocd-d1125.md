---
id: "iss-pyocd-d1125"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Programming several targets in parallel with pyOCD threads fails"
summary: "Each probe flashed fine on its own; a responder doubted that pyOCD's Python API can be used from several threads at once."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1125"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1125"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["HC32F460"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Each probe flashed fine on its own; a responder doubted that pyOCD's Python API can be used from several threads at once.

## Fix

Suggested, not confirmed: run the pyocd command line once per probe with that probe's unique ID, for example from a multiprocessing pool, instead of threads in one process.

## Source

Resolution: workaround

From [pyocd/pyOCD discussion 1125](https://github.com/pyocd/pyOCD/discussions/1125), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
