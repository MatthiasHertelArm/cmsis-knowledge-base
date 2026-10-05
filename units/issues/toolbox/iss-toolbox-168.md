---
id: "iss-toolbox-168"
type: "troubleshooting"
domain: "project"
title: "cbuild: execute scripts do not run when building a single context"
summary: "executes nodes are only processed on full application builds; --context builds one project only, and for-context is only valid in cproject files."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/168"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/168"
resolution: "configuration"
versions: "toolbox 2.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

executes nodes are only processed on full application builds; --context builds one project only, and for-context is only valid in cproject files.

## Fix

Use --context-set (what the VS Code build button does) or build without --context. Place execute nodes in the cproject if they must be per-context.

## Source

Resolution: configuration

Versions: toolbox 2.5.0

From [Open-CMSIS-Pack/cmsis-toolbox #168](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/168), summarized in own words; confidence high, not reviewed yet.
