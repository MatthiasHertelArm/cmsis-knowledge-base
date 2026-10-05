---
id: "iss-pyocd-1460"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Renesas RA pack: flash algorithm not found, target type not recognized"
summary: "The Renesas pack stores its pdsc in a subdirectory; pyOCD found the pdsc but resolved the algorithm paths relative to the archive root."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1460"
doc_source: "https://github.com/pyocd/pyOCD/issues/1460"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["Renesas RA"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Renesas pack stores its pdsc in a subdirectory; pyOCD found the pdsc but resolved the algorithm paths relative to the archive root.

## Fix

pyOCD was to be changed to accept this non-standard layout (PR #1461); use a pyOCD that includes it.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1460](https://github.com/pyocd/pyOCD/issues/1460), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
