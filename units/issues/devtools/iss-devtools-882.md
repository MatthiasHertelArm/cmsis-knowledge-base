---
id: "iss-devtools-882"
type: "troubleshooting"
domain: "project"
title: "cbuild: ERROR M204 path not found: RTE/_Target_1 when the solution has no build-type"
summary: "With a target-type but no build-type, csolution names the file <project>+<target-type>.cprj and the context RTE folder RTE/_<target-type>, but cbuildgen did not treat '+' as separator and looked for the placeholder folder _Target_1, which cbuild does not create by default."
status: "draft"
tool: "cbuild"
symptoms: ["*** ERROR M204:\n  Path not found: '...<projectdir>/RTE/_Target_1'!"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/882"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/882"
resolution: "fixed-in-release"
versions: "Seen in 1.6.0; fixed in 1.7.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M204:
  Path not found: '...<projectdir>/RTE/_Target_1'!`

## Cause

With a target-type but no build-type, csolution names the file <project>+<target-type>.cprj and the context RTE folder RTE/_<target-type>, but cbuildgen did not treat '+' as separator and looked for the placeholder folder _Target_1, which cbuild does not create by default.

## Fix

Add a build-type to the csolution.yml, or run cbuild once with --update-rte so the folder is created. Fixed in CMSIS-Toolbox 1.7.0.

## Source

Resolution: fixed-in-release

Versions: Seen in 1.6.0; fixed in 1.7.0

From [Open-CMSIS-Pack/devtools #882](https://github.com/Open-CMSIS-Pack/devtools/issues/882), summarized in own words; confidence high, checked against the thread, not reviewed yet.
