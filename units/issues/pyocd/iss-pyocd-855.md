---
id: "iss-pyocd-855"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb and SWV together on a CMSIS-DAP probe corrupt each other's responses"
summary: "The SWO polling thread and the transfer thread shared the probe so that their DAP responses were mixed up on probes with SWO via DAP_SWO_Data."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/855"
doc_source: "https://github.com/pyocd/pyOCD/issues/855"
resolution: "fixed-in-release"
versions: "affected 0.2x"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The SWO polling thread and the transfer thread shared the probe so that their DAP responses were mixed up on probes with SWO via DAP_SWO_Data.

## Fix

Fixed in a pyOCD release after 0.26; upgrade.

## Source

Resolution: fixed-in-release

Versions: affected 0.2x

From [pyocd/pyOCD #855](https://github.com/pyocd/pyOCD/issues/855), summarized in own words; confidence medium, not reviewed yet.
