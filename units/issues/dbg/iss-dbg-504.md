---
id: "iss-dbg-504"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD load picks the wrong file type for ELF files with an unusual extension such as .out"
summary: "Without a cbuild-run file pyOCD decides the format from the file extension; IAR produces .out ELF files."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/504"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/504"
resolution: "fixed-in-release"
versions: "fixed in pyOCD 0.39.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Without a cbuild-run file pyOCD decides the format from the file extension; IAR produces .out ELF files.

## Fix

Use pyOCD 0.39.0 or later, which takes the file type from the cbuild-run file; otherwise pass --format elf.

## Source

Resolution: fixed-in-release

Versions: fixed in pyOCD 0.39.0

From [Open-CMSIS-Pack/vscode-cmsis-debugger #504](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/504), summarized in own words; confidence high, checked against the thread, not reviewed yet.
