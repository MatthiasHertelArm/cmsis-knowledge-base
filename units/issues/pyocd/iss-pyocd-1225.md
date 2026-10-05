---
id: "iss-pyocd-1225"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PSoC 5LP kit with KitProg v1 is not detected"
summary: "The CY8CKIT-059 has KitProg (v1), which has no CMSIS-DAP mode; pyOCD supports only KitProg2 in CMSIS-DAP mode and KitProg3."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1225"
doc_source: "https://github.com/pyocd/pyOCD/issues/1225"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CY8CKIT-059 has KitProg (v1), which has no CMSIS-DAP mode; pyOCD supports only KitProg2 in CMSIS-DAP mode and KitProg3. PSoC 5LP devices are not really supported by pyOCD either (no CMSIS-Pack, no flash programming).

## Fix

No fix for this kit in pyOCD; only KitProg2 (switched to CMSIS-DAP mode with its button) or KitProg3 probes are detected.

## Source

Resolution: not-a-bug

From [pyocd/pyOCD #1225](https://github.com/pyocd/pyOCD/issues/1225), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
