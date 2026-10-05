---
id: "iss-devtools-2142"
type: "troubleshooting"
domain: "project"
title: "cbuild: Pre-build execute step output shows up after compiler output"
summary: "Ninja buffers the output of nested builds until the subprocess ends; with ninja --quiet on the nested build of an execute: step the pre-build output was reordered and appeared after the compiler output, although the step really ran first."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2142"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2142"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Ninja buffers the output of nested builds until the subprocess ends; with ninja --quiet on the nested build of an execute: step the pre-build output was reordered and appeared after the compiler output, although the step really ran first.

## Fix

Fixed in a CMSIS-Toolbox nightly build, confirmed by the reporter; the real order of execution was always correct.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #2142](https://github.com/Open-CMSIS-Pack/devtools/issues/2142), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
