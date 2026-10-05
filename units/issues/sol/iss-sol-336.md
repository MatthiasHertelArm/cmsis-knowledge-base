---
id: "iss-sol-336"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Saving Software Components strips packs/components from other contexts' clayer files"
summary: "Saving the Software Components view for one context removed the packs: and components: nodes from .clayer.yml files used only by other contexts, so their board layer no longer referenced the BSP/DFP packs."
status: "draft"
tool: "cmsis-solution"
symptoms: ["board 'KIT_T2G-B-H_LITE:V1' was not found"]
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/336"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/336"
resolution: "fixed-in-release"
versions: "1.68.0 and 1.68.1-9-11630ad affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`board 'KIT_T2G-B-H_LITE:V1' was not found`

## Cause

Saving the Software Components view for one context removed the packs: and components: nodes from .clayer.yml files used only by other contexts, so their board layer no longer referenced the BSP/DFP packs.

## Fix

Fixed in a CMSIS Solution CI build after 1.68.0 (validated from CI artifacts); no release is named.

## Source

Resolution: fixed-in-release

Versions: 1.68.0 and 1.68.1-9-11630ad affected

From [Open-CMSIS-Pack/vscode-cmsis-solution #336](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/336), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
