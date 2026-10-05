---
id: "iss-pyocd-1089"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Probe shows up under a wrong board name after changing the DAP serial string"
summary: "pyOCD maps probe serial-number prefixes to Mbed board IDs, and a bug in the CMSIS-DAP board identification matched an unrelated custom serial string to a u-blox board."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1089"
doc_source: "https://github.com/pyocd/pyOCD/issues/1089"
resolution: "fixed-in-release"
versions: "seen with 0.29"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD maps probe serial-number prefixes to Mbed board IDs, and a bug in the CMSIS-DAP board identification matched an unrelated custom serial string to a u-blox board.

## Fix

Fixed in PR #1090 (included in the next release after 0.29). Board ID background is documented on the pyOCD wiki page 'Board IDs'.

## Source

Resolution: fixed-in-release

Versions: seen with 0.29

From [pyocd/pyOCD #1089](https://github.com/pyocd/pyOCD/issues/1089), summarized in own words; confidence medium, not reviewed yet.
