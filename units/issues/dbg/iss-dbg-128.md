---
id: "iss-dbg-128"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flash programming fails on LPC55S69 when the device is erased"
summary: "Before programming, pyOCD reads flash to compare it with the image; on an erased LPC55S69 these direct reads cause bus errors."
status: "draft"
tool: "pyocd"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/128"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/128"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S69"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Before programming, pyOCD reads flash to compare it with the image; on an erased LPC55S69 these direct reads cause bus errors.

## Fix

Use a pyOCD that skips reading erased sectors when the flash algorithm provides a Verify function, first in the standalone build v0.0.0-standalone-cbuild4.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-debugger #128](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/128), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
