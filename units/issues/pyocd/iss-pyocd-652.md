---
id: "iss-pyocd-652"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list --targets fails with BadZipFile after a broken pack index download"
summary: "cmsis-pack-manager built a wrong download URL for a pack whose index URL lacks a trailing slash, so a garbage file was stored."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'module' object has no attribute 'BadZipFile'"]
symptom_regex: "uncaught\\s+exception:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/652"
doc_source: "https://github.com/pyocd/pyOCD/issues/652"
resolution: "fixed-in-release"
versions: "pyocd 0.20.0 with Python 2.7"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'module' object has no attribute 'BadZipFile'`

## Cause

cmsis-pack-manager built a wrong download URL for a pack whose index URL lacks a trailing slash, so a garbage file was stored. The BadZipFile name does not exist in the Python 2 zipfile module, which hid the real error.

## Fix

Update pyOCD and cmsis-pack-manager (fix released after this report), clear the cache with `pyocd pack --clean`, and meanwhile use a manually downloaded pack via `--pack <file>` or the `pack:` list in pyocd.yaml. Prefer Python 3.

## Source

Resolution: fixed-in-release

Versions: pyocd 0.20.0 with Python 2.7

From [pyocd/pyOCD #652](https://github.com/pyocd/pyOCD/issues/652), summarized in own words; confidence medium, not reviewed yet.
