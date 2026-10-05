---
id: "iss-pyocd-625"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Config file not named pyocd.yaml is ignored, target stays generic cortex_m"
summary: "The target override and test_binary options were placed in a file called test_boards.yaml. pyOCD reads its config from pyocd.yaml (the functional tests switched to that name), so the target stayed at the generic cortex_m type, which has no flash …"
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/625"
doc_source: "https://github.com/pyocd/pyOCD/issues/625"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The target override and test_binary options were placed in a file called test_boards.yaml. pyOCD reads its config from pyocd.yaml (the functional tests switched to that name), so the target stayed at the generic cortex_m type, which has no flash support or memory map.

## Fix

Rename the file to pyocd.yaml and set target_override and test_binary there (or pass --target), then check the 'Target type is ...' log line to confirm the target.

## Source

Resolution: configuration

From [pyocd/pyOCD #625](https://github.com/pyocd/pyOCD/issues/625), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
