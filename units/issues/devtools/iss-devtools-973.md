---
id: "iss-devtools-973"
type: "troubleshooting"
domain: "project"
title: "csolution: misc options of a setup vanish from the cprj when several setups match one context"
summary: "When a context is matched by more than one setup, only the first matching setup is evaluated; its (possibly empty) misc block hides the misc options of later setups, and with the order swapped the defines of the other …"
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/973"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/973"
resolution: "fixed-in-release"
versions: "Seen with 2.0.0-dev0; improved in 2.0.0-dev2"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

When a context is matched by more than one setup, only the first matching setup is evaluated; its (possibly empty) misc block hides the misc options of later setups, and with the order swapped the defines of the other setups get lost.

## Fix

Keep one setup per context and put compiler-specific options into that setup, for example misc entries with a for-compiler: GCC key under the Debug and Release setups. Merging of additive options for several setups was added in CMSIS-Toolbox 2.0.0-dev2.

## Source

Resolution: fixed-in-release

Versions: Seen with 2.0.0-dev0; improved in 2.0.0-dev2

From [Open-CMSIS-Pack/devtools #973](https://github.com/Open-CMSIS-Pack/devtools/issues/973), summarized in own words; confidence medium, not reviewed yet.
