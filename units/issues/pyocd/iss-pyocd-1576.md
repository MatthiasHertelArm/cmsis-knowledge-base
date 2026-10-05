---
id: "iss-pyocd-1576"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: nRF91 auto-unlock fails with a probe that has no nRESET line"
summary: "Unlocking this SiP revision requires pin reset from the probe, which a probe offering only SWCLK and SWDIO cannot provide."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1576"
doc_source: "https://github.com/pyocd/pyOCD/issues/1576"
resolution: "workaround"
versions: "0.35.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "family": ["nRF9160"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Unlocking this SiP revision requires pin reset from the probe, which a probe offering only SWCLK and SWDIO cannot provide.

## Fix

Unlock the device and then power cycle it before reconnecting, or use a probe wired to nRST.

## Source

Resolution: workaround

Versions: 0.35.1

From [pyocd/pyOCD #1576](https://github.com/pyocd/pyOCD/issues/1576), summarized in own words; confidence high, checked against the thread, not reviewed yet.
