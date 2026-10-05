---
id: "iss-dbg-382"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v1 (HID) probes fail on macOS with \"already open\""
summary: "On macOS, opening a CMSIS-DAP v1 (HID) probe timed out, which the reporter put down to a non-working USB connection and a suspected general libusb problem on macOS; the next open attempt then failed with 'already open'."
status: "draft"
tool: "pyocd"
symptoms: ["0100505 C Error: already open [__main__]"]
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/382"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/382"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0100505 C Error: already open [__main__]`

## Cause

On macOS, opening a CMSIS-DAP v1 (HID) probe timed out, which the reporter put down to a non-working USB connection and a suspected general libusb problem on macOS; the next open attempt then failed with 'already open'.

## Fix

Use a pyOCD build with PR 1792 (tested with a separate build; no release named).

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-debugger #382](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/382), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
