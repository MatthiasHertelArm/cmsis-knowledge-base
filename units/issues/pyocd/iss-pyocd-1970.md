---
id: "iss-pyocd-1970"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: J-Link open by serial number fails with 'No emulator with serial number found'"
summary: "With jlink.non_interactive enabled (default), pyOCD disables dialog boxes in the J-Link DLL before opening the probe, and with some DLL versions this breaks opening by serial number."
status: "draft"
tool: "pyocd"
symptoms: ["No emulator with serial number <SN> found."]
symptom_regex: "No\\s+emulator\\s+with\\s+serial\\s+number\\s+<SN>\\s+found\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1970"
doc_source: "https://github.com/pyocd/pyOCD/issues/1970"
resolution: "fixed-in-release"
versions: "seen on 0.44.0 with J-Link DLL 9.24"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No emulator with serial number <SN> found.`

## Cause

With jlink.non_interactive enabled (default), pyOCD disables dialog boxes in the J-Link DLL before opening the probe, and with some DLL versions this breaks opening by serial number.

## Fix

Set 'jlink.non_interactive: false' in pyocd.yaml as a workaround, or upgrade to a pyOCD release with the reordering fix (change #1927).

## Source

Resolution: fixed-in-release

Versions: seen on 0.44.0 with J-Link DLL 9.24

From [pyocd/pyOCD #1970](https://github.com/pyocd/pyOCD/issues/1970), summarized in own words; confidence high, not reviewed yet.
