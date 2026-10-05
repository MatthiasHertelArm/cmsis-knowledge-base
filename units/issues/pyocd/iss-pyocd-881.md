---
id: "iss-pyocd-881"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Erase or flash of LPC55S28 hits an assertion because the core is never halted"
summary: "LPC55xx boot ROM needs special handling to halt after reset; LPC552x had no built-in target so that logic was missing (and it is single-core, unlike LPC55S69)."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/881"
doc_source: "https://github.com/pyocd/pyOCD/issues/881"
resolution: "fixed-in-release"
versions: "seen 0.24 to 0.26.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S28"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

LPC55xx boot ROM needs special handling to halt after reset; LPC552x had no built-in target so that logic was missing (and it is single-core, unlike LPC55S69).

## Fix

Use a pyOCD release with LPC552x support (PR #884 and follow-ups). The workaround of -t lpc55s69 fails because that target assumes two cores.

## Source

Resolution: fixed-in-release

Versions: seen 0.24 to 0.26.1

From [pyocd/pyOCD #881](https://github.com/pyocd/pyOCD/issues/881), summarized in own words; confidence medium, not reviewed yet.
