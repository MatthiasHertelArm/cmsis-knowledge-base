---
id: "iss-devtools-2041"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-run.yml debug-topology lacks processors not used by the selected context"
summary: "csolution listed in debug-topology only the processors used by the selected contexts, but pyOCD examines the complete device at connect and needs the full topology; flash algorithms were filtered the same way (#2026)."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2041"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2041"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution", "pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution listed in debug-topology only the processors used by the selected contexts, but pyOCD examines the complete device at connect and needs the full topology; flash algorithms were filtered the same way (#2026).

## Fix

Fixed by devtools PR #2046, in CMSIS-Toolbox nightly #444 and later: debug-topology lists all processors of the device. Update the toolbox.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #2041](https://github.com/Open-CMSIS-Pack/devtools/issues/2041), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
