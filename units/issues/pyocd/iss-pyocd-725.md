---
id: "iss-pyocd-725"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: mbed LPC1768 not found by pyocd on Windows 10 although mbed-ls lists it"
summary: "The board's old interface firmware exposes only the mass-storage interface under Windows 10; the CMSIS-DAP HID interface never appears, so no debug tool can see it."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/725"
doc_source: "https://github.com/pyocd/pyOCD/issues/725"
resolution: "workaround"
versions: "seen with 0.22.0"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC1768"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The board's old interface firmware exposes only the mass-storage interface under Windows 10; the CMSIS-DAP HID interface never appears, so no debug tool can see it.

## Fix

Update the interface firmware, or install the Mbed composite driver (the serial driver is outdated and unstable on Windows 10).

## Source

Resolution: workaround

Versions: seen with 0.22.0

From [pyocd/pyOCD #725](https://github.com/pyocd/pyOCD/issues/725), summarized in own words; confidence low, not reviewed yet.
