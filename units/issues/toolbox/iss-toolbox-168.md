---
id: "iss-toolbox-168"
type: "troubleshooting"
domain: "project"
title: "cbuild: execute scripts do not run when building a single context"
summary: "executes nodes are only processed on full application builds; --context builds one project only, and for-context is only valid in cproject files (solution-level executes run once)."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/168"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/168"
resolution: "configuration"
versions: "CMSIS-Toolbox 2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

executes nodes are only processed on full application builds; --context builds one project only, and for-context is only valid in cproject files (solution-level executes run once).

## Fix

Build with --context-set but without --context, or without any context option. Place execute nodes in the cproject.yml when they must run per context with for-context.

## Source

Resolution: configuration

Versions: CMSIS-Toolbox 2.5.0

From [Open-CMSIS-Pack/cmsis-toolbox #168](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/168), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
