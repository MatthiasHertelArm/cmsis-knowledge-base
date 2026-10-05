---
id: "iss-devtools-2235"
type: "troubleshooting"
domain: "project"
title: "cbuild: AC6 link step fails on map file option with quoted path (CMake 4.x, macOS)"
summary: "The map file path in the armlink command was wrapped in quote characters that ended up literally in the command, so the link step broke."
status: "draft"
tool: "cbuild"
symptoms: ["armlink --cpu=Cortex-M33 --scatter=<tmp>/ac6_linker_script.sct --map --list=\\\"<out>/TrafficLight.map\\\""]
symptom_regex: "armlink\\s+\\-\\-cpu=Cortex\\-M33\\s+\\-\\-scatter=<tmp>/ac6_linker_script\\.sct\\s+\\-\\-map\\s+\\-\\-list=\\\\\".*?\""
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2235"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2235"
resolution: "fixed-in-release"
versions: "quoting introduced by a change in the 2.9 timeframe, fixed in October 2025 nightly"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild", "csolution"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`armlink --cpu=Cortex-M33 --scatter=<tmp>/ac6_linker_script.sct --map --list=\"<out>/TrafficLight.map\"`

## Cause

The map file path in the armlink command was wrapped in quote characters that ended up literally in the command, so the link step broke.

## Fix

Fixed in a toolbox nightly after 2.9; confirmed building with CMake 4.1.2. Update the toolbox.

## Source

Resolution: fixed-in-release

Versions: quoting introduced by a change in the 2.9 timeframe, fixed in October 2025 nightly

From [Open-CMSIS-Pack/devtools #2235](https://github.com/Open-CMSIS-Pack/devtools/issues/2235), summarized in own words; confidence medium, not reviewed yet.
