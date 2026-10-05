---
id: "iss-cpackget-43"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add .pack: 'has no release tag matching version' with older local pdsc"
summary: "cpackget checked the requested version against the pdsc already registered in .Local (local_repository.pidx) before extracting the pdsc of the pack being installed."
status: "draft"
tool: "cpackget"
symptoms: ["E: The pack's pdsc (<packs>\\.Local\\STMicroelectronics.STM32U5xx_DFP.pdsc) has no release tag matching version \"0.1.1\"", "E: pack version not found in the pdsc file"]
symptom_regex: "E:\\s+The\\s+pack's\\s+pdsc\\s+\\(<packs>\\S+\\)\\s+has\\s+no\\s+release\\s+tag\\s+matching\\s+version\\s+\".*?\""
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/43"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/43"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: The pack's pdsc (<packs>\.Local\STMicroelectronics.STM32U5xx_DFP.pdsc) has no release tag matching version "0.1.1"`
`E: pack version not found in the pdsc file`

## Cause

cpackget checked the requested version against the pdsc already registered in .Local (local_repository.pidx) before extracting the pdsc of the pack being installed.

## Fix

Remove the pack's entry from local_repository.pidx before installing the pack file; the maintainer said he would fix the check.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cpackget #43](https://github.com/Open-CMSIS-Pack/cpackget/issues/43), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
