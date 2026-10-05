---
id: "iss-pyocd-d1679"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Listing probes and installed packs from the pyOCD Python API"
summary: "pyocd list and pyocd pack show are built on Python helpers that a program can call directly."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1679"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1679"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyocd list and pyocd pack show are built on Python helpers that a program can call directly.

## Fix

Use pyocd.core.helpers.ConnectHelper.get_all_connected_probes(blocking=False) to get probe objects with product_name and unique_id, and pyocd.target.pack.pack_target.ManagedPacks.get_installed_packs() for the installed packs (vendor, pack, version, pack file).

## Source

Resolution: configuration

From [pyocd/pyOCD discussion 1679](https://github.com/pyocd/pyOCD/discussions/1679), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
