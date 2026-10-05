---
id: "iss-pyocd-696"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Debug start on Windows hangs with 'Waiting for a debug probe to be connected...'"
summary: "On Windows pyOCD found no libusb library, so STLink and CMSIS-DAP v2 probes were unsupported and the server kept waiting for a probe; 'pip install libusb' did not provide the DLL."
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
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Waiting for a debug probe to be connected...`

## Cause

On Windows pyOCD found no libusb library, so STLink and CMSIS-DAP v2 probes were unsupported and the server kept waiting for a probe; 'pip install libusb' did not provide the DLL.

## Fix

Download libusb from libusb.info and place its DLL next to python.exe, matching the 32- or 64-bit architecture of the Python installation (maintainer's advice, not confirmed in the thread).

## Source

Resolution: configuration

From [pyocd/pyOCD #696](https://github.com/pyocd/pyOCD/issues/696), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
