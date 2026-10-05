---
id: "iss-pyocd-1493"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: ATSAMD21G18A connect fails with No ACK; deprecated Keil pack shadows Microchip pack"
summary: "Two packs describe the same part and the pack cache is keyed by part number, so the deprecated Keil pack for ATSAMD21G18A wins and cannot connect to this chip."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd.probe.pydapaccess.dap_access_api.DAPAccessIntf.TransferError: No ACK received"]
symptom_regex: "pyocd\\.probe\\.pydapaccess\\.dap_access_api\\.DAPAccessIntf\\.TransferError:\\s+No\\s+ACK\\s+received"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1493"
doc_source: "https://github.com/pyocd/pyOCD/issues/1493"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["ATSAMD21G18A"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd.probe.pydapaccess.dap_access_api.DAPAccessIntf.TransferError: No ACK received`

## Cause

Two packs describe the same part and the pack cache is keyed by part number, so the deprecated Keil pack for ATSAMD21G18A wins and cannot connect to this chip.

## Fix

Install the Microchip pack by naming a part only in that pack, for example pyocd pack install ATSAMD21J17D. Alternatively delete the Keil pdsc entry from the local pack cache.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1493](https://github.com/pyocd/pyOCD/issues/1493), summarized in own words; confidence medium, not reviewed yet.
