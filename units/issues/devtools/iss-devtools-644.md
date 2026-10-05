---
id: "iss-devtools-644"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild puts pack include paths before user paths, so duplicate headers shadow local ones"
summary: "csolution lists user add-paths first and pack paths after them in *.cbuild.yml, but the cbuildgen/cprj route ordered them the other way round, so a header present in a DFP shadowed a local copy."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/644"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/644"
resolution: "workaround"
versions: "1.4/1.5 era"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution lists user add-paths first and pack paths after them in *.cbuild.yml, but the cbuildgen/cprj route ordered them the other way round, so a header present in a DFP shadowed a local copy.

## Fix

A fix of the include order in cbuild was decided. For modified DFP files the advised clean solution is a local pack: copy the pack into the project and reference its pdsc instead of the installed one.

## Source

Resolution: workaround

Versions: 1.4/1.5 era

From [Open-CMSIS-Pack/devtools #644](https://github.com/Open-CMSIS-Pack/devtools/issues/644), summarized in own words; confidence medium, not reviewed yet.
