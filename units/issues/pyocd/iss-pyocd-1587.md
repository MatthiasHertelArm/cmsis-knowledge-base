---
id: "iss-pyocd-1587"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: i.MX RT1176 pack target: DebugPortStart not run and second core not created"
summary: "The RT1176 pack defines DebugPortStart per core, which the pack spec does not handle for multi-core debugging."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1587"
doc_source: "https://github.com/pyocd/pyOCD/issues/1587"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["MIMXRT1176DVMAA"], "core": ["Cortex-M7", "Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The RT1176 pack defines DebugPortStart per core, which the pack spec does not handle for multi-core debugging. In addition pyOCD wrongly applied its IMXRT family class to the pack target, and that class creates only the first core.

## Fix

Remove the family match for IMXRT pack targets in pyocd/target/family/__init__.py, or use a build containing the fix of PR 1594, which drops it. Then both cores are found. A branch honouring the pname of the debug sequences only runs DebugPortStart for the core named by the primary_core option. A user script is needed to release the second core.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1587](https://github.com/pyocd/pyOCD/issues/1587), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
