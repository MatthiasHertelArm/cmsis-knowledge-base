---
id: "iss-pyocd-d1679"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Listing probes and installed packs from the pyOCD Python API"
summary: "The CLI commands pyocd list and pyocd pack show are thin wrappers over public helpers that are not mentioned in the main docs."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1679"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1679"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CLI commands pyocd list and pyocd pack show are thin wrappers over public helpers that are not mentioned in the main docs.

## Fix

Use pyocd.core.helpers.ConnectHelper.get_all_connected_probes(blocking=False) to get probe objects with product_name and unique_id, and pyocd.target.pack.pack_target.ManagedPacks.get_installed_packs() for the installed packs (vendor, pack, version, pack file).

## Source

Resolution: configuration

From [pyocd/pyOCD discussion 1679](https://github.com/pyocd/pyOCD/discussions/1679), summarized in own words; confidence medium, not reviewed yet.
