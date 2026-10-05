---
id: "iss-pyocd-1506"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack update aborts with 'relative URL without a base'"
summary: "A pack vendor's index entry has a bad relative URL, and older cmsis-pack-manager versions abort the whole index update on one failing descriptor."
status: "draft"
tool: "pyocd"
symptoms: ["Exception: b'\\nrelative URL without a base'"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1506"
doc_source: "https://github.com/pyocd/pyOCD/issues/1506"
resolution: "workaround"
versions: "Seen with pyocd 0.29 and cmsis-pack-manager 0.3.0."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Exception: b'\nrelative URL without a base'`

## Cause

A pack vendor's index entry has a bad relative URL, and older cmsis-pack-manager versions abort the whole index update on one failing descriptor.

## Fix

Upgrade pyocd and cmsis-pack-manager (pyocd 0.34.3 with cmsis-pack-manager 0.5.2 skips failing descriptors and finishes the update).

## Source

Resolution: workaround

Versions: Seen with pyocd 0.29 and cmsis-pack-manager 0.3.0.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1506](https://github.com/pyocd/pyOCD/issues/1506), summarized in own words; confidence medium, not reviewed yet.
