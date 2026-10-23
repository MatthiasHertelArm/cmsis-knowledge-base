---
id: "iss-pyocd-2060"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v2 probe sends zero-length IN packet after 512-byte reply, desyncing pyOCD"
summary: "When a reply is exactly the DAP packet size (512 bytes), the probe ends the bulk IN transfer with a zero-length packet. pyOCD reads one USB packet per command, so it takes that empty packet as the reply to …"
status: "draft"
tool: "pyocd"
symptoms: ["USBTimeoutError [Errno 10060]", "IndexError: bytearray index out of range"]
symptom_regex: "USBTimeoutError\\s+\\[Errno\\s+\\S+\\]"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2060"
doc_source: "https://github.com/pyocd/pyOCD/issues/2060"
resolution: "workaround"
versions: "pyOCD 0.45.1 (Windows 10, Python 3.14) with the Microchip MPLAB PICkit Basic on CMSIS-DAP v2 firmware switched via pycmsisdapswitcher 2.0.2.19. The fix is in PR #2061; the thread does not say it is released."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "board": ["Microchip MPLAB PICkit Basic"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`USBTimeoutError [Errno 10060]`
`IndexError: bytearray index out of range`

## Cause

When a reply is exactly the DAP packet size (512 bytes), the probe ends the bulk IN transfer with a zero-length packet. pyOCD reads one USB packet per command, so it takes that empty packet as the reply to the next command, and the real reply stays queued in the probe. Every later command then times out until the probe is unplugged and plugged back in.

## Fix

Make the pyOCD USB receive loop (PyUSBv2.rx_task) skip zero-length reads and keep reading until it gets a non-empty packet, since no CMSIS-DAP reply is ever empty. This change is implemented in pull request #2061, which the thread asks to be checked. Block reads of 254 or 255 words trigger the problem on this probe.

## Source

Resolution: workaround

Versions: pyOCD 0.45.1 (Windows 10, Python 3.14) with the Microchip MPLAB PICkit Basic on CMSIS-DAP v2 firmware switched via pycmsisdapswitcher 2.0.2.19. The fix is in PR #2061; the thread does not say it is released.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #2060](https://github.com/pyocd/pyOCD/issues/2060), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
