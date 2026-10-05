---
id: "iss-devtools-2325"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild setup fails because image files in a target-set are not built yet"
summary: "Images listed under target-set images: (for example post-build signed .bin files) were checked as dependencies during setup, and evaluating the $OutDir()$ access sequences created cyclic dependencies, so setup failed before anything could be built."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2325"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2325"
resolution: "fixed-in-release"
versions: "seen before 2.12.0-41"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Images listed under target-set images: (for example post-build signed .bin files) were checked as dependencies during setup, and evaluating the $OutDir()$ access sequences created cyclic dependencies, so setup failed before anything could be built.

## Fix

Fixed in toolbox nightly 2.12.0-41 and later; update. Output directories via $OutDir()$ work afterwards.

## Source

Resolution: fixed-in-release

Versions: seen before 2.12.0-41

From [Open-CMSIS-Pack/devtools #2325](https://github.com/Open-CMSIS-Pack/devtools/issues/2325), summarized in own words; confidence high, checked against the thread, not reviewed yet.
