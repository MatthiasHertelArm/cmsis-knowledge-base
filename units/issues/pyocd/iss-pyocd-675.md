---
id: "iss-pyocd-675"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd gdb as normal user fails on FreeBSD when detaching the kernel HID driver"
summary: "On open, the CMSIS-DAP USB backend tries to detach the kernel driver of the HID interface."
status: "draft"
tool: "pyocd"
symptoms: ["0000749:ERROR:__main__:uncaught exception: [Errno None] Other error"]
symptom_regex: "\\S+:ERROR:__main__:uncaught\\s+exception:\\s+\\[Errno\\s+None\\]\\s+Other\\s+error"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/675"
doc_source: "https://github.com/pyocd/pyOCD/issues/675"
resolution: "fixed-in-release"
versions: "0.19.0 affected; fix merged on master afterwards"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000749:ERROR:__main__:uncaught exception: [Errno None] Other error`

## Cause

On open, the CMSIS-DAP USB backend tries to detach the kernel driver of the HID interface. An unprivileged user may not do that, and the resulting libusb error was not caught, so the session aborted. The detach is not needed for DAPLink to work.

## Fix

Run with a pyOCD that catches errors from the kernel-driver detach and carries on (fixed on master after 0.19.0). As a stop-gap, run as root or patch the detach call out.

## Source

Resolution: fixed-in-release

Versions: 0.19.0 affected; fix merged on master afterwards

From [pyocd/pyOCD #675](https://github.com/pyocd/pyOCD/issues/675), summarized in own words; confidence medium, not reviewed yet.
