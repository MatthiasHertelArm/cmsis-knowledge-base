---
id: "iss-devtools-2141"
type: "troubleshooting"
domain: "project"
title: "cbuild: execute: step with always: seems skipped on the second build"
summary: "always: was honoured and the step did run (the log prints Executing: <context>-<execute name> unconditionally)."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2141"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2141"
resolution: "not-a-bug"
versions: "CMSIS-Toolbox 2.10, CMSIS Solution 1.55.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

always: was honoured and the step did run (the log prints Executing: <context>-<execute name> unconditionally). The step runs CMake over the example's own FCARM/CMakeLists.txt, which checks dependencies and calls FCARM only when they require it.

## Fix

Nothing to fix in cbuild: always: works as documented, and whether FCARM is invoked is decided by the CMakeLists.txt that the execute step builds.

## Source

Resolution: not-a-bug

Versions: CMSIS-Toolbox 2.10, CMSIS Solution 1.55.1

From [Open-CMSIS-Pack/devtools #2141](https://github.com/Open-CMSIS-Pack/devtools/issues/2141), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
