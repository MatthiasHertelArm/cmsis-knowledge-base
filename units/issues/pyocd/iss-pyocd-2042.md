---
id: "iss-pyocd-2042"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Silicon Labs Series 2 packs missing from pack find/install; manual --pack works"
summary: "After a pack update, the local cache holds none of the SiliconLabs index entries, so pack find and pack install cannot see Series 2 devices."
status: "draft"
tool: "pyocd"
symptoms: ["No matching devices"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2042"
doc_source: "https://github.com/pyocd/pyOCD/issues/2042"
resolution: "workaround"
versions: "Reported on pyOCD 0.45.1 with pack 2025.12.1"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["EFR32FG22C121F512GM40"], "pack": ["SiliconLabs.GeckoPlatform_EFR32FG22_DFP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No matching devices`

## Cause

After a pack update, the local cache holds none of the SiliconLabs index entries, so pack find and pack install cannot see Series 2 devices. The reporter suspects the vendor's download host rejects scripted requests with HTTP 403, but this is not confirmed and the thread does not show why the entries are missing.

## Fix

Download the Silicon Labs GeckoPlatform pack for the device family by hand from Silicon Labs' CMSIS pack resources page and pass the file to pyocd with --pack, for example pyocd flash --pack <downloaded .pack> -t <device> <binary>. Pack discovery for these devices remains unresolved in the thread.

## Source

Resolution: workaround

Versions: Reported on pyOCD 0.45.1 with pack 2025.12.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #2042](https://github.com/pyocd/pyOCD/issues/2042), summarized in own words; confidence low, checked against the thread, not reviewed yet.
