---
id: "iss-dbg-100"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyOCD without libusb on macOS cannot connect to CMSIS-DAPv2 probes"
summary: "The bundled pyOCD did not contain libusb."
status: "draft"
tool: "pyocd"
symptoms: ["0001425 W STLink, CMSIS-DAPv2 and PicoProbe probes are not supported because no libusb library was found. [common]"]
symptom_regex: "STLink,\\s+CMSIS\\-DAPv2\\s+and\\s+PicoProbe\\s+probes\\s+are\\s+not\\s+supported\\s+because\\s+no\\s+libusb\\s+library\\s+was\\s+found\\."
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/100"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/100"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001425 W STLink, CMSIS-DAPv2 and PicoProbe probes are not supported because no libusb library was found. [common]`

## Cause

The bundled pyOCD did not contain libusb.

## Fix

Use CMSIS Debugger 0.2+ which bundles libusb.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #100](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/100), summarized in own words; confidence high, not reviewed yet.
