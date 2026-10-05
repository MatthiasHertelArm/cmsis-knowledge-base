---
id: "iss-devtools-175"
type: "troubleshooting"
domain: "project"
title: "csolution: Two DFP packs resolve the same device name; the cprj lists both DFPs"
summary: "The device exists with the same Dvendor and Dname in two installed packs (an official and another vendor's DFP), so csolution may select either."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/175"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/175"
resolution: "workaround"
versions: "csolution 0.9.2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The device exists with the same Dvendor and Dname in two installed packs (an official and another vendor's DFP), so csolution may select either.

## Fix

Reduce the pack scope by installing only the relevant packs; the pack selection mechanism (packs: in csolution.yml) was still under development and not accepted by csolution 0.9.2.

## Source

Resolution: workaround

Versions: csolution 0.9.2

From [Open-CMSIS-Pack/devtools #175](https://github.com/Open-CMSIS-Pack/devtools/issues/175), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
