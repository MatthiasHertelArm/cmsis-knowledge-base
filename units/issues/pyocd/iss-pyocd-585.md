---
id: "iss-pyocd-585"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD cannot find libusb on Windows: 32-bit Python was installed"
summary: "The libusb DLL from the 64-bit folder only loads in a 64-bit Python process."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/585"
doc_source: "https://github.com/pyocd/pyOCD/issues/585"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The libusb DLL from the 64-bit folder only loads in a 64-bit Python process. The user's Python was 32-bit, so only the 32-bit DLL worked.

## Fix

Install 64-bit Python (or match the DLL bitness to the interpreter) and place libusb-1.0.dll where Python finds it.

## Source

Resolution: user-error

From [pyocd/pyOCD #585](https://github.com/pyocd/pyOCD/issues/585), summarized in own words; confidence high, not reviewed yet.
