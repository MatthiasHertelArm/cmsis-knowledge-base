---
id: "iss-devtools-1172"
type: "troubleshooting"
domain: "pack"
title: "cpackget: Local pack clone with pdsc version 0.0.0 loses to installed pack releases"
summary: "A pack whose pdsc gets its release history generated in CI contains only a dummy release 0.0.0 in the working tree."
status: "draft"
tool: "cpackget"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1172"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1172"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A pack whose pdsc gets its release history generated in CI contains only a dummy release 0.0.0 in the working tree. Local repository entries are treated like installed packs, with precedence only for the same version, so any installed release with a higher version wins.

## Fix

Either add a release element to the local pdsc whose version equals or exceeds the newest installed release (and fix the history again before merging), or remove all installed versions of that pack from the pack cache so only the local repository entry remains. Projects with pack version constraints still select the constrained version.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #1172](https://github.com/Open-CMSIS-Pack/devtools/issues/1172), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
