---
id: "iss-devtools-175"
type: "troubleshooting"
domain: "project"
title: "csolution: Two DFP packs resolve the same device name; the cprj lists both DFPs"
summary: "The device exists with the same Dvendor and Dname in two installed packs (for example an official and a vendor-specific DFP), so csolution may select either."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/175"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/175"
resolution: "workaround"
versions: "csolution 0.9.2"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The device exists with the same Dvendor and Dname in two installed packs (for example an official and a vendor-specific DFP), so csolution may select either.

## Fix

Reduce the pack scope: list the wanted DFP under packs: in csolution.yml (pack selection) or install only the relevant packs.

## Source

Resolution: workaround

Versions: csolution 0.9.2

From [Open-CMSIS-Pack/devtools #175](https://github.com/Open-CMSIS-Pack/devtools/issues/175), summarized in own words; confidence medium, not reviewed yet.
