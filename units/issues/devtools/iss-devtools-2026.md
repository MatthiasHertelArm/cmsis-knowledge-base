---
id: "iss-devtools-2026"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-run.yml flash algorithm limited to one processor on multi-core devices"
summary: "csolution collects device data through the RTE model per Pname of the selected contexts, so it wrote a pname for each algorithm even where the pack gave no Pname, which restricted a shared algorithm to a single core."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2026"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2026"
resolution: "fixed-in-release"
versions: "CMSIS-Toolbox 2.8.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "family": ["K32L3A60"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution collects device data through the RTE model per Pname of the selected contexts, so it wrote a pname for each algorithm even where the pack gave no Pname, which restricted a shared algorithm to a single core.

## Fix

Fixed by devtools PR #2039, in CMSIS-Toolbox nightly #435 and later: pname is only written when the pack specifies it.

## Source

Resolution: fixed-in-release

Versions: CMSIS-Toolbox 2.8.0

From [Open-CMSIS-Pack/devtools #2026](https://github.com/Open-CMSIS-Pack/devtools/issues/2026), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
