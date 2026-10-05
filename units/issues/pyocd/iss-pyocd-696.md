---
id: "iss-pyocd-696"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Debug start on Windows hangs with 'Waiting for a debug probe to be connected...'"
summary: "On Windows, STLink and CMSIS-DAP v2 probes need a libusb DLL next to the Python executable, and it must match the Python architecture (32 or 64 bit); without it no probe is found."
status: "draft"
tool: "pyocd"
symptoms: ["Waiting for a debug probe to be connected..."]
symptom_regex: "Waiting\\s+for\\s+a\\s+debug\\s+probe\\s+to\\s+be\\s+connected\\.\\.\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/696"
doc_source: "https://github.com/pyocd/pyOCD/issues/696"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Waiting for a debug probe to be connected...`

## Cause

On Windows, STLink and CMSIS-DAP v2 probes need a libusb DLL next to the Python executable, and it must match the Python architecture (32 or 64 bit); without it no probe is found.

## Fix

Download libusb, put the DLL of the matching bitness next to python.exe as the README says, then run `pyocd list` to check.

## Source

Resolution: configuration

From [pyocd/pyOCD #696](https://github.com/pyocd/pyOCD/issues/696), summarized in own words; confidence medium, not reviewed yet.
