---
id: "iss-pyocd-925"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd gdb fails loading the J-Link library with 'wrong ELF class: ELFCLASS32'"
summary: "pyOCD's J-Link support loads the SEGGER shared library through pylink-square at startup; a 32-bit J-Link library on a 64-bit Python (or the reverse), or a badly located library, makes the load fail for every command."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: /tmp/tmp1gi3hg44.so: wrong ELF class: ELFCLASS32"]
symptom_regex: "uncaught\\s+exception:\\s+\\S+:\\s+wrong\\s+ELF\\s+class:\\s+ELFCLASS32"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/925"
doc_source: "https://github.com/pyocd/pyOCD/issues/925"
resolution: "workaround"
versions: "seen with 0.27.x on Linux"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: /tmp/tmp1gi3hg44.so: wrong ELF class: ELFCLASS32`

## Cause

pyOCD's J-Link support loads the SEGGER shared library through pylink-square at startup; a 32-bit J-Link library on a 64-bit Python (or the reverse), or a badly located library, makes the load fail for every command.

## Fix

Reinstall the J-Link software package matching the Python bitness. Uninstalling J-Link makes the error disappear but also disables J-Link probes in pyOCD.

## Source

Resolution: workaround

Versions: seen with 0.27.x on Linux

From [pyocd/pyOCD #925](https://github.com/pyocd/pyOCD/issues/925), summarized in own words; confidence low, not reviewed yet.
