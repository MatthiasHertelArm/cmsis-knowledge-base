---
id: "iss-pyocd-1646"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Erase/load fails with IPSR=3 after upgrading to 0.36 on Cortex-M0 devices"
summary: "The flash algorithm was started with the Thumb bit clear in xPSR, which faults on Cortex-M."
status: "draft"
tool: "pyocd"
symptoms: ["W T bit in XPSR is invalid; the vector table may be invalid or corrupt [cortex_m]", "C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]"]
symptom_regex: "W\\s+T\\s+bit\\s+in\\s+XPSR\\s+is\\s+invalid;\\s+the\\s+vector\\s+table\\s+may\\s+be\\s+invalid\\s+or\\s+corrupt"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1646"
doc_source: "https://github.com/pyocd/pyOCD/issues/1646"
resolution: "fixed-in-release"
versions: "broken 0.35/0.36, fixed 0.37.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "core": ["Cortex-M0"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W T bit in XPSR is invalid; the vector table may be invalid or corrupt [cortex_m]`
`C target was not halted as expected after calling flash algorithm routine (IPSR=3) [__main__]`

## Cause

The flash algorithm was started with the Thumb bit clear in xPSR, which faults on Cortex-M.

## Fix

Fixed in 0.37.0 by writing the Thumb bit before running algorithm functions; upgrade.

## Source

Resolution: fixed-in-release

Versions: broken 0.35/0.36, fixed 0.37.0

From [pyocd/pyOCD #1646](https://github.com/pyocd/pyOCD/issues/1646), summarized in own words; confidence high, not reviewed yet.
