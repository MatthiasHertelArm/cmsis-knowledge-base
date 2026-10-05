---
id: "iss-devtools-2339"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution cannot find cproject.yml when names contain non-ASCII characters on Windows"
summary: "csolution 2.11.0 on Windows corrupts non-ASCII characters in file names and paths (an encoding issue), so it cannot find the referenced cproject.yml."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2339"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2339"
resolution: "workaround"
versions: "2.11.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution 2.11.0 on Windows corrupts non-ASCII characters in file names and paths (an encoding issue), so it cannot find the referenced cproject.yml. CMake also restricts the characters of target names, which are formed from project names, target types, build types and execute names.

## Fix

Workaround: enable the Windows option 'Beta: Use Unicode UTF-8 for worldwide language support' (system-wide, may affect legacy tools). Keep project names, target types, build types and execute names ASCII. A documentation note was requested.

## Source

Resolution: workaround

Versions: 2.11.0

From [Open-CMSIS-Pack/devtools #2339](https://github.com/Open-CMSIS-Pack/devtools/issues/2339), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
