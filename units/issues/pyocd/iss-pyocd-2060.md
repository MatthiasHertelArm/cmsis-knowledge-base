---
id: "iss-pyocd-2060"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v2 zero-length IN packet after 512-byte reply desyncs pyOCD (PICkit Basic)"
summary: "When a CMSIS-DAP reply is exactly the packet size (512 bytes), the probe ends the bulk IN transfer with a zero-length packet. pyOCD reads one USB packet per command, so it takes that empty packet as the reply to …"
status: "draft"
tool: "pyocd"
symptoms: ["IndexError: bytearray index out of range", "USBTimeoutError [Errno 10060]"]
symptom_regex: "IndexError:\\s+bytearray\\s+index\\s+out\\s+of\\s+range"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2060"
doc_source: "https://github.com/pyocd/pyOCD/issues/2060"
resolution: "workaround"
versions: "pyOCD 0.45.1 on Windows 10 with a Microchip PICkit Basic running CMSIS-DAP v2 firmware; the fix is in PR #2061 and the thread does not show a release."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["nRF51822"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`IndexError: bytearray index out of range`
`USBTimeoutError [Errno 10060]`

## Cause

When a CMSIS-DAP reply is exactly the packet size (512 bytes), the probe ends the bulk IN transfer with a zero-length packet. pyOCD reads one USB packet per command, so it takes that empty packet as the reply to the next command. The real reply is then left unread in the probe, and every later command times out.

## Fix

In the PyUSBv2 receive task, read again whenever a read returns zero bytes, and only pass non-empty data on to the reply queue, since no valid CMSIS-DAP reply is empty. Pull request #2061 implements this workaround; the thread says the probe should not send the zero-length packet, so the probe-side behaviour is the underlying defect.

## Source

Resolution: workaround

Versions: pyOCD 0.45.1 on Windows 10 with a Microchip PICkit Basic running CMSIS-DAP v2 firmware; the fix is in PR #2061 and the thread does not show a release.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #2060](https://github.com/pyocd/pyOCD/issues/2060), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
