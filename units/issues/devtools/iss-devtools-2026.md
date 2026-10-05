---
id: "iss-devtools-2026"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-run.yml flash algorithm limited to one processor on multi-core devices"
summary: "csolution wrote a pname for each algorithm based on the processors of the selected contexts, even where the pack gave no Pname, which restricted a shared algorithm to a single core."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2026"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2026"
resolution: "fixed-in-release"
versions: "seen in 2.8"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "family": ["K32L3A60"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution wrote a pname for each algorithm based on the processors of the selected contexts, even where the pack gave no Pname, which restricted a shared algorithm to a single core.

## Fix

Fixed in toolbox nightly 435 (April 2025) and later; pname is only written when the pack specifies it.

## Source

Resolution: fixed-in-release

Versions: seen in 2.8

From [Open-CMSIS-Pack/devtools #2026](https://github.com/Open-CMSIS-Pack/devtools/issues/2026), summarized in own words; confidence high, not reviewed yet.
