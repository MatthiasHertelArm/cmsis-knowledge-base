---
id: "iss-pyocd-1472"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PyInstaller build cannot load cmsis_pack_manager native library or plugins"
summary: "The frozen app lacks the native cmsis_pack_manager module and libusb library, so plugin loading fails and no probe is found."
status: "draft"
tool: "pyocd"
symptoms: ["OSError: cannot load library"]
symptom_regex: "OSError:\\s+cannot\\s+load\\s+library"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1472"
doc_source: "https://github.com/pyocd/pyOCD/issues/1472"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`OSError: cannot load library`

## Cause

The frozen app lacks the native cmsis_pack_manager module and libusb library, so plugin loading fails and no probe is found.

## Fix

Add the libusb DLL and the cmsis_pack_manager native module as data/binaries in the PyInstaller spec (see the pyOCD discussion on binary builds).

## Source

Resolution: workaround

From [pyocd/pyOCD #1472](https://github.com/pyocd/pyOCD/issues/1472), summarized in own words; confidence medium, not reviewed yet.
