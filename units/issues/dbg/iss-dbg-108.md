---
id: "iss-dbg-108"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: GDB server exits with \"RW section does not follow RO section\""
summary: "pyOCD checked the flash algorithm layout too strictly and ignored section alignment."
status: "draft"
tool: "pyocd"
symptoms: ["0001679 C RW section does not follow RO section [__main__]"]
symptom_regex: "RW\\s+section\\s+does\\s+not\\s+follow\\s+RO\\s+section"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/108"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/108"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["T2G"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001679 C RW section does not follow RO section [__main__]`

## Cause

pyOCD checked the flash algorithm layout too strictly and ignored section alignment.

## Fix

Use a pyOCD with PR 1795 (CMSIS Debugger 1.0.0 and later).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #108](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/108), summarized in own words; confidence high, not reviewed yet.
