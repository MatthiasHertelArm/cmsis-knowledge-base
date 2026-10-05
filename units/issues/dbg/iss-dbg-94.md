---
id: "iss-dbg-94"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Auto-detection fails on NXP K32L3A6 multi-core device"
summary: "Debug-topology missing from cbuild-run; DFP 19.0.0 listed wrong AP index for the M0+."
status: "draft"
tool: "pyocd"
symptoms: ["0001184 C Error: <APv1Address@0x1e77c825b50 #2 dp=0> [__main__]"]
symptom_regex: "Error:\\s+<APv1Address@\\S+\\s+\\#\\S+\\s+dp=\\S+>"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/94"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/94"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["K32L3A6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0001184 C Error: <APv1Address@0x1e77c825b50 #2 dp=0> [__main__]`

## Cause

Debug-topology missing from cbuild-run; DFP 19.0.0 listed wrong AP index for the M0+.

## Fix

Add debug-topology with cm4 apid 0 index 0 and cm0plus apid 1 index 2 to the cbuild-run file, or use a corrected DFP and newer toolbox.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/vscode-cmsis-debugger #94](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/94), summarized in own words; confidence high, not reviewed yet.
