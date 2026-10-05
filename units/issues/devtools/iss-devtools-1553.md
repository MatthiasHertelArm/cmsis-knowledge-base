---
id: "iss-devtools-1553"
type: "troubleshooting"
domain: "project"
title: "csolution: Schema 2.3 rejects cbuild.yml files written by toolbox 2.1/2.2 (from-pack missing)"
summary: "Schema version 2.3 made from-pack required for generators, but cbuild.yml files written by cbuild 2.1/2.2 do not contain it, so validating them with that schema fails."
status: "draft"
tool: "csolution"
symptoms: ["missing properties: 'from-pack'"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1553"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1553"
resolution: "workaround"
versions: "schema 2.3; cbuild 2.1, 2.2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`missing properties: 'from-pack'`

## Cause

Schema version 2.3 made from-pack required for generators, but cbuild.yml files written by cbuild 2.1/2.2 do not contain it, so validating them with that schema fails.

## Fix

Remove from-pack from the required list of the generator entry so it is optional (the reporter patched the schema this way); the maintainers agreed to make this change, but the thread shows no release with it.

## Source

Resolution: workaround

Versions: schema 2.3; cbuild 2.1, 2.2

From [Open-CMSIS-Pack/devtools #1553](https://github.com/Open-CMSIS-Pack/devtools/issues/1553), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
