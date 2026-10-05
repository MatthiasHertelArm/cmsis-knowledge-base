---
id: "iss-pyocd-1491"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack find or install returns nothing after pack update"
summary: "The maintainer suggested that cmsis-pack-manager 0.5.1 can fail pdsc downloads because too many are started concurrently, leaving the index incomplete; this might explain the reports, but nobody confirmed it."
status: "draft"
tool: "pyocd"
symptoms: ["W No matching devices. Please make sure the pack index is up to date. [pack_cmd]"]
symptom_regex: "W\\s+No\\s+matching\\s+devices\\.\\s+Please\\s+make\\s+sure\\s+the\\s+pack\\s+index\\s+is\\s+up\\s+to\\s+date\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1491"
doc_source: "https://github.com/pyocd/pyOCD/issues/1491"
resolution: "workaround"
versions: "pyOCD 0.34.3 with cmsis-pack-manager 0.5.1; cmsis-pack-manager 0.5.2 addresses the download failures"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W No matching devices. Please make sure the pack index is up to date. [pack_cmd]`

## Cause

The maintainer suggested that cmsis-pack-manager 0.5.1 can fail pdsc downloads because too many are started concurrently, leaving the index incomplete; this might explain the reports, but nobody confirmed it.

## Fix

Update cmsis-pack-manager to 0.5.2 (pip install -U cmsis-pack-manager), which addresses the concurrent-download failures, and run pyocd pack update again.

## Source

Resolution: workaround

Versions: pyOCD 0.34.3 with cmsis-pack-manager 0.5.1; cmsis-pack-manager 0.5.2 addresses the download failures

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1491](https://github.com/pyocd/pyOCD/issues/1491), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
