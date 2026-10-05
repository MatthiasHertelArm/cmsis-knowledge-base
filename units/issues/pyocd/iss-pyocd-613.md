---
id: "iss-pyocd-613"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list -p crashes with a utf16 decode error on old ST-Link firmware"
summary: "ST-Link firmware older than V2J28 reports a USB interface name with an odd number of bytes, which cannot be decoded as UTF-16."
status: "draft"
tool: "pyocd"
symptoms: ["0000387:ERROR:__main__:uncaught exception: 'utf16' codec can't decode byte 0x6c in position 30: truncated data"]
symptom_regex: "\\S+:ERROR:__main__:uncaught\\s+exception:\\s+'.*?'\\s+codec\\s+can't\\s+decode\\s+byte\\s+\\S+\\s+in\\s+position\\s+\\S+:\\s+truncated\\s+data"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/613"
doc_source: "https://github.com/pyocd/pyOCD/issues/613"
resolution: "fixed-in-release"
versions: "ST-Link firmware V2J27 and below"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000387:ERROR:__main__:uncaught exception: 'utf16' codec can't decode byte 0x6c in position 30: truncated data`

## Cause

ST-Link firmware older than V2J28 reports a USB interface name with an odd number of bytes, which cannot be decoded as UTF-16.

## Fix

Update pyOCD to a version with the workaround (change #616, 0.20.0 era); updating the ST-Link firmware also helps.

## Source

Resolution: fixed-in-release

Versions: ST-Link firmware V2J27 and below

From [pyocd/pyOCD #613](https://github.com/pyocd/pyOCD/issues/613), summarized in own words; confidence high, not reviewed yet.
