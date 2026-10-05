---
id: "iss-pyocd-d1416"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT control block address and range cannot be set in the pyOCD YAML config"
summary: "At the time of the discussion the RTT settings existed only as command line options of the rtt command and were not session options, so putting them into the config file had no effect."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/discussions/1416"
doc_source: "https://github.com/pyocd/pyOCD/discussions/1416"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

At the time of the discussion the RTT settings existed only as command line options of the rtt command and were not session options, so putting them into the config file had no effect. Session options are listed in the options reference of the documentation.

## Fix

Pass the RTT control block address and size on the command line instead of the config file.

## Source

Resolution: workaround

From [pyocd/pyOCD discussion 1416](https://github.com/pyocd/pyOCD/discussions/1416), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
