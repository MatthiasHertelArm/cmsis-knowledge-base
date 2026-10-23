---
id: "iss-pyocd-2042"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Series 2 Silicon Labs packs not found by pack find/install; manual --pack works"
summary: "The local pack cache used by pyOCD holds no Silicon Labs .pdsc files, so pack find and pack install cannot see Series 2 devices, although the Keil index lists them."
status: "draft"
tool: "pyocd"
symptoms: ["No matching devices", "Error probing AP#3: SWD/JTAG communication failure (WAIT ACK)"]
symptom_regex: "Error\\s+probing\\s+AP\\#\\S+:\\s+SWD/JTAG\\s+communication\\s+failure\\s+\\(WAIT\\s+ACK\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2042"
doc_source: "https://github.com/pyocd/pyOCD/issues/2042"
resolution: "workaround"
versions: "pyOCD 0.45.1; GeckoPlatform_EFR32FG22_DFP 2025.12.1"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["EFR32FG22C121F512GM40"], "pack": ["SiliconLabs.GeckoPlatform_EFR32FG22_DFP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No matching devices`
`Error probing AP#3: SWD/JTAG communication failure (WAIT ACK)`

## Cause

The local pack cache used by pyOCD holds no Silicon Labs .pdsc files, so pack find and pack install cannot see Series 2 devices, although the Keil index lists them. Scripted requests to silabs.com return HTTP 403 in the reporter's environment; whether this causes the missing cache entries is unconfirmed. A manually downloaded pack file bypasses the cache entirely.

## Fix

Download the Silicon Labs Series 2 .pack file (for example SiliconLabs.GeckoPlatform_EFR32FG22_DFP) from Silicon Labs' CMSIS-pack page in a browser, then pass it directly with pyocd flash --pack <file> -t <device>. To silence the AP#3 probe error on Series 2 parts, set adi.v5.max_invalid_ap_count=0. The thread reports that the workaround works, but no maintainer fix is recorded.

## Source

Resolution: workaround

Versions: pyOCD 0.45.1; GeckoPlatform_EFR32FG22_DFP 2025.12.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #2042](https://github.com/pyocd/pyOCD/issues/2042), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
