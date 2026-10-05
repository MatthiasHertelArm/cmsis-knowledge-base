---
id: "iss-pyocd-1694"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Executable built with PyInstaller reports 'No connected debug probes'"
summary: "PyInstaller does not collect pyOCD's probe and RTOS plug-ins (package entry points) and package data by default, so the built executable finds no probe."
status: "draft"
tool: "pyocd"
symptoms: ["No connected debug probes"]
symptom_regex: "No\\s+connected\\s+debug\\s+probes"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1694"
doc_source: "https://github.com/pyocd/pyOCD/issues/1694"
resolution: "workaround"
versions: "seen on 0.36; binaries from v0.38.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No connected debug probes`

## Cause

PyInstaller does not collect pyOCD's probe and RTOS plug-ins (package entry points) and package data by default, so the built executable finds no probe.

## Fix

Collect the 'pyocd.probe' and 'pyocd.rtos' entry points and add the pyocd and pylink package folders as data in the .spec file. On another PC the ST-Link driver may also be needed. Releases from v0.38.0 include prebuilt binaries.

## Source

Resolution: workaround

Versions: seen on 0.36; binaries from v0.38.0

From [pyocd/pyOCD #1694](https://github.com/pyocd/pyOCD/issues/1694), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
