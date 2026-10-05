---
id: "iss-pyocd-925"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd gdb fails loading the J-Link library with 'wrong ELF class: ELFCLASS32'"
summary: "pylink-square, used by pyOCD for J-Link probes, fails to load the SEGGER J-Link library while pyOCD looks for probes."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: /tmp/tmp1gi3hg44.so: wrong ELF class: ELFCLASS32"]
symptom_regex: "uncaught\\s+exception:\\s+\\S+:\\s+wrong\\s+ELF\\s+class:\\s+ELFCLASS32"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/925"
doc_source: "https://github.com/pyocd/pyOCD/issues/925"
resolution: "workaround"
versions: "0.27.1.dev28; pylink-square 1.2.0"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: /tmp/tmp1gi3hg44.so: wrong ELF class: ELFCLASS32`

## Cause

pylink-square, used by pyOCD for J-Link probes, fails to load the SEGGER J-Link library while pyOCD looks for probes. The maintainer suspected a 32/64-bit mismatch; a later commenter found the library bitness made no difference and links it to a pylink-square library-loading problem on Linux (square/pylink#33).

## Fix

Uninstalling the J-Link software removed the error, but this disables J-Link probes in pyOCD; the maintainer also suggested reinstalling the J-Link driver package.

## Source

Resolution: workaround

Versions: 0.27.1.dev28; pylink-square 1.2.0

From [pyocd/pyOCD #925](https://github.com/pyocd/pyOCD/issues/925), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
