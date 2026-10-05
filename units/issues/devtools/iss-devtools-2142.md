---
id: "iss-devtools-2142"
type: "troubleshooting"
domain: "project"
title: "cbuild: Pre-build execute step output shows up after compiler output"
summary: "A nested CMake/Ninja build started by an execute: step was run with ninja --quiet, and Ninja buffers the output of the subprocess until it ends, so messages of the pre-build step appeared to come last."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2142"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2142"
resolution: "fixed-in-release"
versions: "seen around 2.9"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A nested CMake/Ninja build started by an execute: step was run with ninja --quiet, and Ninja buffers the output of the subprocess until it ends, so messages of the pre-build step appeared to come last.

## Fix

Fixed in a toolbox nightly from July 2025 that no longer passes --quiet; the real order of execution was always correct.

## Source

Resolution: fixed-in-release

Versions: seen around 2.9

From [Open-CMSIS-Pack/devtools #2142](https://github.com/Open-CMSIS-Pack/devtools/issues/2142), summarized in own words; confidence high, not reviewed yet.
