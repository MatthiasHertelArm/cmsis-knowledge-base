---
id: "iss-pyocd-1257"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: nRF52 flash over CMSIS-DAP on macOS fails with DAP_TRANSFER response error"
summary: "Command packets arrived out of order or mixed up with a custom CMSIS-DAP firmware at high USB performance."
status: "draft"
tool: "pyocd"
symptoms: ["DAP_TRANSFER response error"]
symptom_regex: "DAP_TRANSFER\\s+response\\s+error"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1257"
doc_source: "https://github.com/pyocd/pyOCD/issues/1257"
resolution: "workaround"
versions: "0.32.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DAP_TRANSFER response error`

## Cause

Command packets arrived out of order or mixed up with a custom CMSIS-DAP firmware at high USB performance.

## Fix

Add -Ocmsis_dap.limit_packets (the =True form was broken until change #1259) and rebase the firmware on current DAPLink.

## Source

Resolution: workaround

Versions: 0.32.1

From [pyocd/pyOCD #1257](https://github.com/pyocd/pyOCD/issues/1257), summarized in own words; confidence medium, not reviewed yet.
