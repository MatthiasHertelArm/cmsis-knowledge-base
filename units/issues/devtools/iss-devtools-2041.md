---
id: "iss-devtools-2041"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-run.yml debug-topology lacks processors not used by the selected context"
summary: "csolution filtered debug topology and flash algorithm data by the pname of the selected context, but pyOCD examines the whole device when connecting and needs the complete topology."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2041"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2041"
resolution: "fixed-in-release"
versions: "seen in 2.8 to 2.9 timeframe"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution", "pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution filtered debug topology and flash algorithm data by the pname of the selected context, but pyOCD examines the whole device when connecting and needs the complete topology.

## Fix

Fixed in toolbox nightly 444 (April 2025) and later: debug-topology lists all debug ports and processors of the device. Update the toolbox.

## Source

Resolution: fixed-in-release

Versions: seen in 2.8 to 2.9 timeframe

From [Open-CMSIS-Pack/devtools #2041](https://github.com/Open-CMSIS-Pack/devtools/issues/2041), summarized in own words; confidence high, not reviewed yet.
