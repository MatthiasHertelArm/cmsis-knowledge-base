---
id: "iss-pyocd-2009"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd hangs forever on first connect with hidapi backend on Windows"
summary: "The hidapi USB backend on Windows had no read timeout, so a read that never completes blocks the process and it cannot exit."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2009"
doc_source: "https://github.com/pyocd/pyOCD/issues/2009"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The hidapi USB backend on Windows had no read timeout, so a read that never completes blocks the process and it cannot exit.

## Fix

Update to a pyOCD release that includes the fix for the hidapi read timeout (change #2011).

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #2009](https://github.com/pyocd/pyOCD/issues/2009), summarized in own words; confidence medium, not reviewed yet.
