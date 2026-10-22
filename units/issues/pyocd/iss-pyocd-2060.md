---
id: "iss-pyocd-2060"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v2 zero-length IN packet after 512-byte reply desyncs pyOCD reads"
summary: "A CMSIS-DAP v2 probe (Microchip PICkit Basic) ends an IN transfer with a zero-length packet when the reply is exactly the DAP packet size, here 512 bytes. pyOCD reads one USB packet per command, so the empty packet is …"
status: "draft"
tool: "pyocd"
symptoms: ["IndexError: bytearray index out of range", "USBTimeoutError [Errno 10060]"]
symptom_regex: "IndexError:\\s+bytearray\\s+index\\s+out\\s+of\\s+range"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2060"
doc_source: "https://github.com/pyocd/pyOCD/issues/2060"
resolution: "workaround"
versions: "pyOCD 0.45.1 with Microchip PICkit Basic CMSIS-DAP v2 firmware on Windows 10; workaround in PR #2061."
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

A CMSIS-DAP v2 probe (Microchip PICkit Basic) ends an IN transfer with a zero-length packet when the reply is exactly the DAP packet size, here 512 bytes. pyOCD reads one USB packet per command, so the empty packet is taken as the reply to the next command. The real reply stays in the probe and every later command is out of step until the probe is replugged.

## Fix

Make the receive task in pyOCD's CMSIS-DAP v2 backend ignore zero-length reads and keep reading until it gets data, since no valid CMSIS-DAP reply is empty. PR #2061 implements this workaround; the thread does not show it merged or released. The probe firmware should stop sending the zero-length packet, which the maintainer says is the proper fix.

## Source

Resolution: workaround

Versions: pyOCD 0.45.1 with Microchip PICkit Basic CMSIS-DAP v2 firmware on Windows 10; workaround in PR #2061.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #2060](https://github.com/pyocd/pyOCD/issues/2060), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
