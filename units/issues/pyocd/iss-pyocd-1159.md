---
id: "iss-pyocd-1159"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd flash on FreeBSD fails with ImportError for ENODATA from errno"
summary: "pyusb referenced an errno constant that exists only on Linux, so the USB backend failed on FreeBSD when opening a CMSIS-DAP probe."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: cannot import name 'ENODATA' from 'errno' (unknown location)"]
symptom_regex: "uncaught\\s+exception:\\s+cannot\\s+import\\s+name\\s+'.*?'\\s+from\\s+'.*?'\\s+\\(unknown\\s+location\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1159"
doc_source: "https://github.com/pyocd/pyOCD/issues/1159"
resolution: "fixed-in-release"
versions: "affected: pyusb before 1.2.1 on FreeBSD; fixed by pyusb 1.2.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: cannot import name 'ENODATA' from 'errno' (unknown location)`

## Cause

pyusb referenced an errno constant that exists only on Linux, so the USB backend failed on FreeBSD when opening a CMSIS-DAP probe.

## Fix

Use pyusb 1.2.1 or newer, which contains the fix; pyOCD raised its minimum pyusb requirement accordingly.

## Source

Resolution: fixed-in-release

Versions: affected: pyusb before 1.2.1 on FreeBSD; fixed by pyusb 1.2.1

From [pyocd/pyOCD #1159](https://github.com/pyocd/pyOCD/issues/1159), summarized in own words; confidence high, not reviewed yet.
