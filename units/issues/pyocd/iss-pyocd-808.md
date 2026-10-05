---
id: "iss-pyocd-808"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing MIMXRT1050-EVKB fails with 'No ACK received' or 'No cores were discovered'"
summary: "The on-board DAPLink firmware was an old release (254) that lacked fixes for this board that existed in DAPLink master."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd.probe.pydapaccess.dap_access_api.DAPAccessIntf.TransferError: No ACK received", "pyocd.core.exceptions.DebugError: No cores were discovered!"]
symptom_regex: "pyocd\\.probe\\.pydapaccess\\.dap_access_api\\.DAPAccessIntf\\.TransferError:\\s+No\\s+ACK\\s+received"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/808"
doc_source: "https://github.com/pyocd/pyOCD/issues/808"
resolution: "workaround"
versions: "seen with 0.24.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MIMXRT1050"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd.probe.pydapaccess.dap_access_api.DAPAccessIntf.TransferError: No ACK received`
`pyocd.core.exceptions.DebugError: No cores were discovered!`

## Cause

The on-board DAPLink firmware was an old release (254) that lacked fixes for this board that existed in DAPLink master.

## Fix

Update the board's DAPLink interface firmware to a build that includes the later fixes.

## Source

Resolution: workaround

Versions: seen with 0.24.1

From [pyocd/pyOCD #808](https://github.com/pyocd/pyOCD/issues/808), summarized in own words; confidence medium, not reviewed yet.
