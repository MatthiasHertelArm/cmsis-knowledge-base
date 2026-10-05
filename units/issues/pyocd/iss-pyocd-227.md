---
id: "iss-pyocd-227"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Repeated flashing from a Linux VM randomly hangs"
summary: "USB transfers in some virtual machines (VirtualBox, VMware) can stall without a timeout."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/227"
doc_source: "https://github.com/pyocd/pyOCD/issues/227"
resolution: "workaround"
versions: "0.7.x"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

USB transfers in some virtual machines (VirtualBox, VMware) can stall without a timeout. A timeout was later added to the pyusb backend.

## Fix

Use a pyOCD with USB timeouts, or run natively; resetting the target first with the tool avoided the hang.

## Source

Resolution: workaround

Versions: 0.7.x

From [pyocd/pyOCD #227](https://github.com/pyocd/pyOCD/issues/227), summarized in own words; confidence low, not reviewed yet.
