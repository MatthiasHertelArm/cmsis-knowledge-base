---
id: "iss-pyocd-881"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Erase or flash of LPC55S28 hits an assertion because the core is never halted"
summary: "The LPC55xx boot ROM needs custom handling to halt after reset; the LPC552x had no built-in target so that logic was not used, and the -t lpc55s69 workaround fails because the LPC552x is single-core while the LPC55S69 target assumes …"
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/881"
doc_source: "https://github.com/pyocd/pyOCD/issues/881"
resolution: "fixed-in-release"
versions: "0.24.0, 0.25.0, 0.26.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S28"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The LPC55xx boot ROM needs custom handling to halt after reset; the LPC552x had no built-in target so that logic was not used, and the -t lpc55s69 workaround fails because the LPC552x is single-core while the LPC55S69 target assumes two cores.

## Fix

Use pyOCD with the later changes: the single-core handling of PR #884 resolved the halt failure, and #885 added LPC55S28 support with an updated flash algorithm. The reporter still saw a chip-erase hang with the development head.

## Source

Resolution: fixed-in-release

Versions: 0.24.0, 0.25.0, 0.26.1

From [pyocd/pyOCD #881](https://github.com/pyocd/pyOCD/issues/881), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
