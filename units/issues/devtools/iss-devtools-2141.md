---
id: "iss-devtools-2141"
type: "troubleshooting"
domain: "project"
title: "cbuild: execute: step with always: seems skipped on the second build"
summary: "always: was honoured and the step did run (the log prints Executing: <context>-<execute name>)."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2141"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2141"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

always: was honoured and the step did run (the log prints Executing: <context>-<execute name>). The step itself starts an inner CMake project that checks its own dependencies and so decides not to regenerate the output.

## Fix

Put the dependency logic in the inner CMakeLists (inputs and outputs of the real tool) or remove the dependency check there. The step still runs on each build if always: is set.

## Source

Resolution: not-a-bug

From [Open-CMSIS-Pack/devtools #2141](https://github.com/Open-CMSIS-Pack/devtools/issues/2141), summarized in own words; confidence medium, not reviewed yet.
