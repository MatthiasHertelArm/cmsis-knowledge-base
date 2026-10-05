---
id: "iss-pyocd-949"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing a .bin fails: pack has a flash algorithm but no flash memory element"
summary: "The device pack defines a flash algorithm for an address range but has no matching memory element for that flash, so pyocd finds no flash region."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/949"
doc_source: "https://github.com/pyocd/pyOCD/issues/949"
resolution: "configuration"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "family": ["LPC54018M"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The device pack defines a flash algorithm for an address range but has no matching memory element for that flash, so pyocd finds no flash region.

## Fix

Add a memory element for the flash range to a local copy of the pack and pass it with --pack (or the pack session option). A pyocd change to derive a region from an algorithm without a memory was on the todo list.

## Source

Resolution: configuration

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #949](https://github.com/pyocd/pyOCD/issues/949), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
