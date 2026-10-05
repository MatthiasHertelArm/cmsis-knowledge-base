---
id: "iss-cpackget-43"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add .pack: 'has no release tag matching version' with older local pdsc"
summary: "cpackget validated the version against the pdsc already registered in .Local instead of the pdsc inside the pack being installed."
status: "draft"
tool: "cpackget"
symptoms: ["E: The pack's pdsc (<packs>\\.Local\\STMicroelectronics.STM32U5xx_DFP.pdsc) has no release tag matching version \"0.1.1\"", "E: pack version not found in the pdsc file"]
symptom_regex: "E:\\s+The\\s+pack's\\s+pdsc\\s+\\(<packs>\\S+\\)\\s+has\\s+no\\s+release\\s+tag\\s+matching\\s+version\\s+\".*?\""
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/43"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/43"
resolution: "fixed-in-release"
versions: "2022"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: The pack's pdsc (<packs>\.Local\STMicroelectronics.STM32U5xx_DFP.pdsc) has no release tag matching version "0.1.1"`
`E: pack version not found in the pdsc file`

## Cause

cpackget validated the version against the pdsc already registered in .Local instead of the pdsc inside the pack being installed.

## Fix

Use a cpackget after 0.4.x where the pack's own pdsc is extracted first; as a workaround remove the local_repository.pidx entry before installing.

## Source

Resolution: fixed-in-release

Versions: 2022

From [Open-CMSIS-Pack/cpackget #43](https://github.com/Open-CMSIS-Pack/cpackget/issues/43), summarized in own words; confidence medium, not reviewed yet.
