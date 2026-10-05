---
id: "iss-pyocd-2031"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pack-based reset fails with FAULT ACK on ATSAM4L since pyOCD 0.44"
summary: "When a CMSIS-Pack defines no ResetSystem sequence, pyOCD 0.44 and later run a new built-in default reset sequence."
status: "draft"
tool: "pyocd"
symptoms: ["Memory transfer fault (Error while running debug sequence 'ResetSystem' (core Cortex-M4): Memory transfer fault (SWD/JTAG communication failure (FAULT ACK)))"]
symptom_regex: "Memory\\s+transfer\\s+fault\\s+\\(Error\\s+while\\s+running\\s+debug\\s+sequence\\s+'.*?'\\s+\\(core\\s+Cortex\\-M4\\):\\s+Memory\\s+transfer\\s+fault\\s+\\(SWD/JTAG\\s+communication\\s+failure\\s+\\(FAULT\\s+ACK\\)\\)\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2031"
doc_source: "https://github.com/pyocd/pyOCD/issues/2031"
resolution: "workaround"
versions: "Regression from v0.44.0; still present in v0.45.1."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["ATSAM4LS8C"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Memory transfer fault (Error while running debug sequence 'ResetSystem' (core Cortex-M4): Memory transfer fault (SWD/JTAG communication failure (FAULT ACK)))`

## Cause

When a CMSIS-Pack defines no ResetSystem sequence, pyOCD 0.44 and later run a new built-in default reset sequence. On this Cortex-M4 part that default fails with a FAULT ACK, while the generic reset without the pack still works.

## Fix

Override the reset type so pyOCD uses its own SYSRESETREQ implementation instead of the default pack sequence: add -Oreset_type=sysresetreq to the reset, flash or load command. Confirmed to restore flashing.

## Source

Resolution: workaround

Versions: Regression from v0.44.0; still present in v0.45.1.

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #2031](https://github.com/pyocd/pyOCD/issues/2031), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
