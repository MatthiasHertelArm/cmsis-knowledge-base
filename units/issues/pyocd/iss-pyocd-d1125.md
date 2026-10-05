---
id: "iss-pyocd-d1125"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Programming several targets in parallel with pyOCD threads fails"
summary: "The pyOCD Python API is not designed to be driven from several threads at once, so parallel flashing in threads over separate probes can fail even though each probe works alone."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1125"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1125"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["HC32F460"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The pyOCD Python API is not designed to be driven from several threads at once, so parallel flashing in threads over separate probes can fail even though each probe works alone.

## Fix

Start one pyocd command line process per probe (each with its own --probe unique ID), for example from a multiprocessing pool, instead of using threads in one process.

## Source

Resolution: workaround

From [pyocd/pyOCD discussion 1125](https://github.com/pyocd/pyOCD/discussions/1125), summarized in own words; confidence low, not reviewed yet.
