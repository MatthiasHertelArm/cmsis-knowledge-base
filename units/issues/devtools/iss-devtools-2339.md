---
id: "iss-devtools-2339"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution cannot find cproject.yml when names contain non-ASCII characters on Windows"
summary: "csolution passes UTF-8 strings from YAML and JSON to std::filesystem without conversion to the Windows code page, so paths with non-ASCII characters get corrupted."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2339"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2339"
resolution: "workaround"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution passes UTF-8 strings from YAML and JSON to std::filesystem without conversion to the Windows code page, so paths with non-ASCII characters get corrupted. CMake additionally restricts target names (project, build type, target type, execute names) to a limited character set.

## Fix

Workaround: enable the Windows option Beta Use Unicode UTF-8 for worldwide language support (system-wide, may affect legacy tools). Keep project, type and execute names ASCII. A documentation note was requested.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #2339](https://github.com/Open-CMSIS-Pack/devtools/issues/2339), summarized in own words; confidence high, not reviewed yet.
