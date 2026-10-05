---
id: "iss-devtools-263"
type: "troubleshooting"
domain: "project"
title: "csolution: add-paths ignored or error when used under files or repeated as map keys"
summary: "add-paths is accepted for a single file, a group, a component, the project, a layer, the solution and build or target types, but not for the files list, and it only affects the sources compiled at that level, so …"
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/263"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/263"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

add-paths is accepted for a single file, a group, a component, the project, a layer, the solution and build or target types, but not for the files list, and it only affects the sources compiled at that level, so a path given for a group does not reach a component's sources. Repeating the add-paths key in one map is invalid YAML because keys must be unique.

## Fix

Put the include path where the failing source is compiled: on the component that needs it (e.g. Device:STM32Cube HAL:Common) or at project level, and write several paths as one list (add-paths: [., ./targets/board] or one entry per line).

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #263](https://github.com/Open-CMSIS-Pack/devtools/issues/263), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
