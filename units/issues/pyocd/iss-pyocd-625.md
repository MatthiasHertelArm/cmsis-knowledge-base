---
id: "iss-pyocd-625"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Config file not named pyocd.yaml is ignored, target stays generic cortex_m"
summary: "The target override and test_binary options were placed in a file called test_boards.yaml. pyOCD only reads a config named pyocd.yaml, so the target stayed at the generic cortex_m type, which has no flash or memory map."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/625"
doc_source: "https://github.com/pyocd/pyOCD/issues/625"
resolution: "configuration"
versions: "0.19 to 0.20"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The target override and test_binary options were placed in a file called test_boards.yaml. pyOCD only reads a config named pyocd.yaml, so the target stayed at the generic cortex_m type, which has no flash or memory map.

## Fix

Name the file pyocd.yaml (or give it with --config), set target_override and test_binary there, and check the log line 'Target type is ...' to confirm which target is used.

## Source

Resolution: configuration

Versions: 0.19 to 0.20

From [pyocd/pyOCD #625](https://github.com/pyocd/pyOCD/issues/625), summarized in own words; confidence high, not reviewed yet.
