---
id: "iss-pyocd-1225"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PSoC 5LP kit with KitProg v1 is not detected"
summary: "That kit's programmer has no CMSIS-DAP mode, and pyOCD supports only KitProg2/3 in CMSIS-DAP mode; PSoC 5LP is not supported either."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1225"
doc_source: "https://github.com/pyocd/pyOCD/issues/1225"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

That kit's programmer has no CMSIS-DAP mode, and pyOCD supports only KitProg2/3 in CMSIS-DAP mode; PSoC 5LP is not supported either.

## Fix

Use a vendor tool or a kit with KitProg3 or KitProg2 in CMSIS-DAP mode.

## Source

Resolution: not-a-bug

From [pyocd/pyOCD #1225](https://github.com/pyocd/pyOCD/issues/1225), summarized in own words; confidence medium, not reviewed yet.
