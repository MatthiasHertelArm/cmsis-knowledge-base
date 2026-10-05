---
id: "iss-pyocd-1962"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: load --cbuild-run: post-load hardware reset breaks SWD without ResetHardware sequence"
summary: "From 0.42.0 the load command defaults the post-reset to a hardware reset when the cbuild-run file has no load-setup section."
status: "draft"
tool: "pyocd"
symptoms: ["Error while running debug sequence 'DebugCoreStop' (core Cortex-M0+): SWD/JTAG communication failure (No ACK) [cbuild_run]"]
symptom_regex: "Error\\s+while\\s+running\\s+debug\\s+sequence\\s+'.*?'\\s+\\(core\\s+Cortex\\-M0\\+\\):\\s+SWD/JTAG\\s+communication\\s+failure\\s+\\(No\\s+ACK\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1962"
doc_source: "https://github.com/pyocd/pyOCD/issues/1962"
resolution: "fixed-in-release"
versions: "introduced 0.42.0, fixed 0.44.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error while running debug sequence 'DebugCoreStop' (core Cortex-M0+): SWD/JTAG communication failure (No ACK) [cbuild_run]`

## Cause

From 0.42.0 the load command defaults the post-reset to a hardware reset when the cbuild-run file has no load-setup section. On devices whose pack lacks a custom ResetHardware sequence, the plain nRESET also resets the debug port and reconnecting fails, even though programming succeeded.

## Fix

Upgrade to 0.44.1, which reworked post-reset handling. Meanwhile pass '-O load.post_reset=sysresetreq' to pyocd load.

## Source

Resolution: fixed-in-release

Versions: introduced 0.42.0, fixed 0.44.1

From [pyocd/pyOCD #1962](https://github.com/pyocd/pyOCD/issues/1962), summarized in own words; confidence high, checked against the thread, not reviewed yet.
