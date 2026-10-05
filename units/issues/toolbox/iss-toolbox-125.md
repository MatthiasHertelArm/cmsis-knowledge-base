---
id: "iss-toolbox-125"
type: "troubleshooting"
domain: "project"
title: "csolution: CubeMX generator run fails with exit code 1 / required pack not installed"
summary: "The *.cbuild-pack.yml locks the pack version that was current at conversion, while another (dev) version is installed."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: required pack: Keil::B-U585I-IOT02A_BSP@2.0.0-dev0 not installed"]
symptom_regex: "required\\s+pack:\\s+Keil::B\\-U585I\\-IOT02A_BSP@\\S+\\-dev0\\s+not\\s+installed"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/125"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/125"
resolution: "configuration"
versions: "toolbox 2.3.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: required pack: Keil::B-U585I-IOT02A_BSP@2.0.0-dev0 not installed`

## Cause

The *.cbuild-pack.yml locks the pack version that was current at conversion, while another (dev) version is installed.

## Fix

Edit the version in cbuild-pack.yml or run with --load latest to use the latest installed packs.

## Source

Resolution: configuration

Versions: toolbox 2.3.0

From [Open-CMSIS-Pack/cmsis-toolbox #125](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/125), summarized in own words; confidence high, checked against the thread, not reviewed yet.
