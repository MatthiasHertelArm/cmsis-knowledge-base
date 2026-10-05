---
id: "iss-pyocd-227"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Repeated flashing from a Linux VM randomly hangs"
summary: "Not determined."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/227"
doc_source: "https://github.com/pyocd/pyOCD/issues/227"
resolution: "workaround"
versions: "K64F interface firmware 0226"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Not determined. The reporter ran Ubuntu in VMware Player (it was also seen on Raspbian, not on Windows); the maintainer suspected the VM USB problem of #154, for which a timeout was added to the pyusb backend.

## Fix

Run `pyocd-tool -b <id> reset` before each flash command, which prevented the freeze for the reporter; the maintainer said the timeout added to the pyusb backend should fix it if it is the #154 problem.

## Source

Resolution: workaround

Versions: K64F interface firmware 0226

From [pyocd/pyOCD #227](https://github.com/pyocd/pyOCD/issues/227), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
