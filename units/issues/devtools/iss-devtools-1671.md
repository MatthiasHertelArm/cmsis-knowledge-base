---
id: "iss-devtools-1671"
type: "troubleshooting"
domain: "project"
title: "csolution: board with vendor prefix not found although the pack is installed"
summary: "csolution 2.5.0 built the board id with the device vendor (Dvendor 'ABOV Semiconductor') instead of the board's vendor 'ABOV', so the board ABOV::StarterKit-A31G112CL:V1.1 was not found."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: board 'ABOV::StarterKit-A31G112CL:V1.1' was not found"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1671"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1671"
resolution: "fixed-in-release"
versions: "2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: board 'ABOV::StarterKit-A31G112CL:V1.1' was not found`

## Cause

csolution 2.5.0 built the board id with the device vendor (Dvendor 'ABOV Semiconductor') instead of the board's vendor 'ABOV', so the board ABOV::StarterKit-A31G112CL:V1.1 was not found.

## Fix

Use a csolution nightly after 2.5.0, which computes the board id correctly; csolution list boards -f A31G112 then prints ABOV::StarterKit-A31G112CL:V1.1.

## Source

Resolution: fixed-in-release

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1671](https://github.com/Open-CMSIS-Pack/devtools/issues/1671), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
