---
id: "iss-pyocd-1925"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: J-Link fails to open with 'No emulator with serial number' on newer J-Link DLLs"
summary: "A known issue between pylink and J-Link DLL versions 9.14 and above: opening the probe by serial number fails at random."
status: "draft"
tool: "pyocd"
symptoms: ["pylink.errors.JLinkException: No emulator with serial number 1064xxxxx2 found."]
symptom_regex: "pylink\\.errors\\.JLinkException:\\s+No\\s+emulator\\s+with\\s+serial\\s+number\\s+1064xxxxx2\\s+found\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1925"
doc_source: "https://github.com/pyocd/pyOCD/issues/1925"
resolution: "fixed-in-release"
versions: "J-Link DLL above 9.12, reproduced up to 9.26 (V9.16a and V9.22 reported)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pylink.errors.JLinkException: No emulator with serial number 1064xxxxx2 found.`

## Cause

A known issue between pylink and J-Link DLL versions 9.14 and above: opening the probe by serial number fails at random. One user suspected several pylink.JLink instances alive at once; the maintainer saw them destroyed as expected.

## Fix

Use a pyOCD build containing change #1927 (the issue was closed as resolved without a test report). On Windows some dialog boxes may then appear.

## Source

Resolution: fixed-in-release

Versions: J-Link DLL above 9.12, reproduced up to 9.26 (V9.16a and V9.22 reported)

From [pyocd/pyOCD #1925](https://github.com/pyocd/pyOCD/issues/1925), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
