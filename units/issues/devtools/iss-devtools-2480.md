---
id: "iss-devtools-2480"
type: "troubleshooting"
domain: "project"
title: "csolution: Scatter file reported missing right after creating a project from a pack example"
summary: "The example project is not fully configured: its cproject.yml references the scatter file explicitly under linker:, but the RTE config files are not yet present because the extension does not run update-rte when it loads an existing solution."
status: "draft"
tool: "csolution"
symptoms: ["file '<project>/RTE/Device/<device>/<name>.sct' was not found"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2480"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2480"
resolution: "configuration"
versions: "2.13.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`file '<project>/RTE/Device/<device>/<name>.sct' was not found`

## Cause

The example project is not fully configured: its cproject.yml references the scatter file explicitly under linker:, but the RTE config files are not yet present because the extension does not run update-rte when it loads an existing solution. A reload creates them.

## Fix

Reload or refresh the solution, which runs update-rte. Lasting fix is in the example: keep the scatter file in the project tree and reference it, instead of relying on the component config file.

## Source

Resolution: configuration

Versions: 2.13.0

From [Open-CMSIS-Pack/devtools #2480](https://github.com/Open-CMSIS-Pack/devtools/issues/2480), summarized in own words; confidence high, not reviewed yet.
