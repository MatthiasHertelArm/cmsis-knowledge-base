---
id: "iss-devtools-412"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution convert uses lots of memory when the solution lists no packs"
summary: "Without a packs section csolution loaded every installed pack, which can exhaust memory in CI or cloud environments."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/412"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/412"
resolution: "fixed-in-release"
versions: "fixed in 1.2.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Without a packs section csolution loaded every installed pack, which can exhaust memory in CI or cloud environments.

## Fix

Since csolution 1.2.0 only the latest pack versions are loaded by default; use --load required to load only the packs named in csolution.yml (fails if none are listed), or --load all for the old behaviour.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.2.0

From [Open-CMSIS-Pack/devtools #412](https://github.com/Open-CMSIS-Pack/devtools/issues/412), summarized in own words; confidence high, not reviewed yet.
