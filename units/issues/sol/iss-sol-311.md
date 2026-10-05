---
id: "iss-sol-311"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Deselecting the secure project removes Secure_CMSE_Lib.o; non-secure build fails"
summary: "The non-secure project uses $cmse-lib(CM33_s)$ from the secure build output; if that project is not part of the build the library does not exist, and the out folder is regenerated."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/311"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/311"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The non-secure project uses $cmse-lib(CM33_s)$ from the secure build output; if that project is not part of the build the library does not exist, and the out folder is regenerated.

## Fix

Add a target-type (for example AVH-NS-only) whose set builds only the non-secure project and reference ../out/<secure>/<target>/$BuildType$/<lib>.o with for-context; build the full target first. Use load: none in the set to skip programming the secure part.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/vscode-cmsis-solution #311](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/311), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
