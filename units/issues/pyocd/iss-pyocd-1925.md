---
id: "iss-pyocd-1925"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: J-Link fails to open with 'No emulator with serial number' on newer J-Link DLLs"
summary: "A known incompatibility between pylink and J-Link DLL versions above about 9.12: opening by serial number fails, apparently after dialog boxes are disabled or several JLink instances are created."
status: "draft"
tool: "pyocd"
symptoms: ["pylink.errors.JLinkException: No emulator with serial number 1064xxxxx2 found."]
symptom_regex: "pylink\\.errors\\.JLinkException:\\s+No\\s+emulator\\s+with\\s+serial\\s+number\\s+1064xxxxx2\\s+found\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1925"
doc_source: "https://github.com/pyocd/pyOCD/issues/1925"
resolution: "fixed-in-release"
versions: "J-Link DLL 9.14 to 9.26"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pylink.errors.JLinkException: No emulator with serial number 1064xxxxx2 found.`

## Cause

A known incompatibility between pylink and J-Link DLL versions above about 9.12: opening by serial number fails, apparently after dialog boxes are disabled or several JLink instances are created.

## Fix

Use a pyOCD build containing change #1927 (reorders disabling of dialog boxes). On Windows some dialog boxes may then reappear.

## Source

Resolution: fixed-in-release

Versions: J-Link DLL 9.14 to 9.26

From [pyocd/pyOCD #1925](https://github.com/pyocd/pyOCD/issues/1925), summarized in own words; confidence medium, not reviewed yet.
