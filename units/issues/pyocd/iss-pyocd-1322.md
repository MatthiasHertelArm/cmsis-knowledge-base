---
id: "iss-pyocd-1322"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: 0.33.0: 'USB Error: Operation timed out' on pyocd list"
summary: "Appeared with v0.33.0, which newly provisioned libusb through the libusb-package dependency; v0.32.3 with a separately installed libusb worked."
status: "draft"
tool: "pyocd"
symptoms: ["C USB Error: [Errno 10060] Operation timed out [__main__]"]
symptom_regex: "C\\s+USB\\s+Error:\\s+\\[Errno\\s+\\S+\\]\\s+Operation\\s+timed\\s+out"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1322"
doc_source: "https://github.com/pyocd/pyOCD/issues/1322"
resolution: "workaround"
versions: "0.33.0, 0.32.3"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C USB Error: [Errno 10060] Operation timed out [__main__]`

## Cause

Appeared with v0.33.0, which newly provisioned libusb through the libusb-package dependency; v0.32.3 with a separately installed libusb worked. The maintainer could not reproduce it.

## Fix

Stay on v0.32.3; the maintainer planned v0.33.1 to revert the bundled libusb. Updating the ST-Link firmware helped one user only until the probe was replugged. Generic checks suggested: USB access rights, connect directly rather than via a hub, try another port or cable, make sure nothing else uses the device, try the system libusb.

## Source

Resolution: workaround

Versions: 0.33.0, 0.32.3

From [pyocd/pyOCD #1322](https://github.com/pyocd/pyOCD/issues/1322), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
