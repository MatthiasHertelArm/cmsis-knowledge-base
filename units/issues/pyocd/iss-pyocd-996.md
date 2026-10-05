---
id: "iss-pyocd-996"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver launched by Cortex-Debug exits at once; GDB reports connection refused"
summary: "A bug in 0.28.2 made the deprecated pyocd-gdbserver entry point terminate right after start, so the GDB client could not connect."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/996"
doc_source: "https://github.com/pyocd/pyOCD/issues/996"
resolution: "fixed-in-release"
versions: "affected 0.28.2; fixed in 0.28.3"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A bug in 0.28.2 made the deprecated pyocd-gdbserver entry point terminate right after start, so the GDB client could not connect.

## Fix

Upgrade to pyOCD 0.28.3 or later, or use `pyocd gdbserver` instead of the deprecated pyocd-gdbserver command.

## Source

Resolution: fixed-in-release

Versions: affected 0.28.2; fixed in 0.28.3

From [pyocd/pyOCD #996](https://github.com/pyocd/pyOCD/issues/996), summarized in own words; confidence high, not reviewed yet.
