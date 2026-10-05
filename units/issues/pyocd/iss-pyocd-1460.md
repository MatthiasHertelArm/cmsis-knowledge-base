---
id: "iss-pyocd-1460"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Renesas RA pack: flash algorithm not found, target type not recognized"
summary: "The Renesas pack stores its pdsc in a subdirectory; pyOCD found it but resolved algorithm paths relative to the archive root."
status: "draft"
tool: "pyocd"
symptoms: ["KeyError: \"There is no item named 'Flash/RA2A1_256K.FLM' in the archive\""]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1460"
doc_source: "https://github.com/pyocd/pyOCD/issues/1460"
resolution: "fixed-in-release"
versions: "0.34"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["Renesas RA"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`KeyError: "There is no item named 'Flash/RA2A1_256K.FLM' in the archive"`

## Cause

The Renesas pack stores its pdsc in a subdirectory; pyOCD found it but resolved algorithm paths relative to the archive root.

## Fix

Fixed by change #1461 which supports the non-standard layout; upgrade.

## Source

Resolution: fixed-in-release

Versions: 0.34

From [pyocd/pyOCD #1460](https://github.com/pyocd/pyOCD/issues/1460), summarized in own words; confidence high, not reviewed yet.
