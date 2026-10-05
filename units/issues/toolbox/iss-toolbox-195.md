---
id: "iss-toolbox-195"
type: "troubleshooting"
domain: "project"
title: "cbuild: Files in nested groups are compiled without -g and -O options"
summary: "cbuild 2.6.1 did not pass the -g and -O compile options to files placed in nested sub-groups, so no debug info was produced and breakpoints could not be set."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/195"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/195"
resolution: "fixed-in-release"
versions: "cbuild 2.6.1 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

cbuild 2.6.1 did not pass the -g and -O compile options to files placed in nested sub-groups, so no debug info was produced and breakpoints could not be set.

## Fix

Use a CMSIS-Toolbox nightly with the fix, which the reporter confirmed; no release is named. Until then keep such files out of nested groups.

## Source

Resolution: fixed-in-release

Versions: cbuild 2.6.1 affected

From [Open-CMSIS-Pack/cmsis-toolbox #195](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/195), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
