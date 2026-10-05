---
id: "iss-pyocd-1694"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Executable built with PyInstaller reports 'No connected debug probes'"
summary: "PyInstaller does not bundle pyOCD's probe plugins (entry points), the libusb DLL and native extensions by default, so no probe backend loads."
status: "draft"
tool: "pyocd"
symptoms: ["No connected debug probes"]
symptom_regex: "No\\s+connected\\s+debug\\s+probes"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1694"
doc_source: "https://github.com/pyocd/pyOCD/issues/1694"
resolution: "workaround"
versions: "seen on 0.36"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No connected debug probes`

## Cause

PyInstaller does not bundle pyOCD's probe plugins (entry points), the libusb DLL and native extensions by default, so no probe backend loads.

## Fix

Collect the 'pyocd.probe' and 'pyocd.rtos' entry points, pyocd and pylink package data and the libusb DLL in the .spec file. Releases from 0.38.0 provide prebuilt binaries.

## Source

Resolution: workaround

Versions: seen on 0.36

From [pyocd/pyOCD #1694](https://github.com/pyocd/pyOCD/issues/1694), summarized in own words; confidence medium, not reviewed yet.
