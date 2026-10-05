---
id: "iss-pyocd-1491"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack find or install returns nothing after pack update"
summary: "cmsis-pack-manager 0.5.1 started too many descriptor downloads at once, so many pdsc downloads failed and the index was incomplete."
status: "draft"
tool: "pyocd"
symptoms: ["W No matching devices. Please make sure the pack index is up to date. [pack_cmd]"]
symptom_regex: "W\\s+No\\s+matching\\s+devices\\.\\s+Please\\s+make\\s+sure\\s+the\\s+pack\\s+index\\s+is\\s+up\\s+to\\s+date\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1491"
doc_source: "https://github.com/pyocd/pyOCD/issues/1491"
resolution: "workaround"
versions: "cmsis-pack-manager 0.5.1 affected; 0.5.2 fixes."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W No matching devices. Please make sure the pack index is up to date. [pack_cmd]`

## Cause

cmsis-pack-manager 0.5.1 started too many descriptor downloads at once, so many pdsc downloads failed and the index was incomplete.

## Fix

Update cmsis-pack-manager to 0.5.2 or newer (pip install -U cmsis-pack-manager), run pyocd pack update again.

## Source

Resolution: workaround

Versions: cmsis-pack-manager 0.5.1 affected; 0.5.2 fixes.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1491](https://github.com/pyocd/pyOCD/issues/1491), summarized in own words; confidence medium, not reviewed yet.
