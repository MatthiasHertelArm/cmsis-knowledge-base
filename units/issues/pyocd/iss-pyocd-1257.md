---
id: "iss-pyocd-1257"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: nRF52 flash over CMSIS-DAP on macOS fails with DAP_TRANSFER response error"
summary: "Command packets appear to get out of order, dropped or mixed up between pyOCD on macOS and a custom CMSIS-DAP firmware (private DAPLink fork on a K22F); the maintainer suspected the Ubuntu VM worked only because of lower USB performance."
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
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DAP_TRANSFER response error`

## Cause

Command packets appear to get out of order, dropped or mixed up between pyOCD on macOS and a custom CMSIS-DAP firmware (private DAPLink fork on a K22F); the maintainer suspected the Ubuntu VM worked only because of lower USB performance.

## Fix

Add -Ocmsis_dap.limit_packets=1 (the =True form was not accepted until change #1259); the maintainer also suggested rebasing the firmware on the current DAPLink develop branch.

## Source

Resolution: workaround

Versions: 0.32.1

From [pyocd/pyOCD #1257](https://github.com/pyocd/pyOCD/issues/1257), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
