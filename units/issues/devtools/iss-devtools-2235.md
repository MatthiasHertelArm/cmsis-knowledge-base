---
id: "iss-devtools-2235"
type: "troubleshooting"
domain: "project"
title: "cbuild: AC6 link step fails on map file option with quoted path (CMake 4.x, macOS)"
summary: "Quotation marks around the map file path, introduced by devtools PR #2129, ended up literally in the armlink --list option, so the link step broke."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2235"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2235"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "csolution"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Quotation marks around the map file path, introduced by devtools PR #2129, ended up literally in the armlink --list option, so the link step broke.

## Fix

Fixed in the then latest CMSIS-Toolbox nightly; the reporter confirmed building with CMake 4.1.2 and a correctly generated map file. Update the toolbox.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #2235](https://github.com/Open-CMSIS-Pack/devtools/issues/2235), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
