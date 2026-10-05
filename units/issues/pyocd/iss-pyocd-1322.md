---
id: "iss-pyocd-1322"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: 0.33.0: 'USB Error: Operation timed out' on pyocd list"
summary: "Seen with the bundled libusb of 0.33.0 and some ST-Link probes; updating ST-Link firmware helped some users."
status: "draft"
tool: "pyocd"
symptoms: ["C USB Error: [Errno 10060] Operation timed out [__main__]"]
symptom_regex: "C\\s+USB\\s+Error:\\s+\\[Errno\\s+\\S+\\]\\s+Operation\\s+timed\\s+out"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1322"
doc_source: "https://github.com/pyocd/pyOCD/issues/1322"
resolution: "workaround"
versions: "0.33.0"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C USB Error: [Errno 10060] Operation timed out [__main__]`

## Cause

Seen with the bundled libusb of 0.33.0 and some ST-Link probes; updating ST-Link firmware helped some users.

## Fix

Use 0.33.1 (which dropped the bundled libusb), update the probe firmware, check USB permissions or try another port or cable.

## Source

Resolution: workaround

Versions: 0.33.0

From [pyocd/pyOCD #1322](https://github.com/pyocd/pyOCD/issues/1322), summarized in own words; confidence low, not reviewed yet.
