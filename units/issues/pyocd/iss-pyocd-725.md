---
id: "iss-pyocd-725"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: mbed LPC1768 not found by pyocd on Windows 10 although mbed-ls lists it"
summary: "The mbed LPC1768 interface firmware (rev 141212) exposes only the USB mass-storage interface under Windows 10; the CMSIS-DAP HID interface never appears, so no debugger can see the probe and pyOCD cannot fix it."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/725"
doc_source: "https://github.com/pyocd/pyOCD/issues/725"
resolution: "unresolved"
versions: "0.22.0; interface firmware rev 141212"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["LPC1768"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The mbed LPC1768 interface firmware (rev 141212) exposes only the USB mass-storage interface under Windows 10; the CMSIS-DAP HID interface never appears, so no debugger can see the probe and pyOCD cannot fix it.

## Fix

The thread gives no confirmed fix.

## Source

Resolution: unresolved

Versions: 0.22.0; interface firmware rev 141212

From [pyocd/pyOCD #725](https://github.com/pyocd/pyOCD/issues/725), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
