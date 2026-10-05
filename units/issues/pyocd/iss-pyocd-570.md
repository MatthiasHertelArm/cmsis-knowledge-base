---
id: "iss-pyocd-570"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver rejects pack-defined targets with 'invalid target option'"
summary: "The deprecated pyocd-gdbserver tool validates the --target name against built-in targets only (validate_target() in pyocd/tools/gdb_server.py), so pack targets are rejected, while the new `pyocd gdbserver` accepts them."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd-gdbserver: error: invalid target option 'efm32g890f128'"]
symptom_regex: "pyocd\\-gdbserver:\\s+error:\\s+invalid\\s+target\\s+option\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/570"
doc_source: "https://github.com/pyocd/pyOCD/issues/570"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd-gdbserver: error: invalid target option 'efm32g890f128'`

## Cause

The deprecated pyocd-gdbserver tool validates the --target name against built-in targets only (validate_target() in pyocd/tools/gdb_server.py), so pack targets are rejected, while the new `pyocd gdbserver` accepts them.

## Fix

Launch `pyocd gdbserver --pack <file> -t <target>` instead of pyocd-gdbserver (for example in an IDE debug configuration such as cortex-debug).

## Source

Resolution: workaround

From [pyocd/pyOCD #570](https://github.com/pyocd/pyOCD/issues/570), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
