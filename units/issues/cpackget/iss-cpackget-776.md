---
id: "iss-cpackget-776"
type: "troubleshooting"
domain: "pack"
title: "cpackget: Cannot remove a local pack entry whose pdsc file was deleted"
summary: "A pack registered via its pdsc file stays in .Local/local_repository.pidx after the pdsc is deleted."
status: "draft"
tool: "cpackget"
symptoms: ["E: Pack \"arm::sds@3.0.0-dev\" is not installed", "E: pack not installed"]
symptom_regex: "E:\\s+Pack\\s+\".*?\"\\s+is\\s+not\\s+installed"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/776"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/776"
resolution: "workaround"
versions: "CMSIS-Toolbox 2.14.1, cpackget 2.2.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Pack "arm::sds@3.0.0-dev" is not installed`
`E: pack not installed`

## Cause

A pack registered via its pdsc file stays in .Local/local_repository.pidx after the pdsc is deleted. In the report, removing by packID with the version failed, and the attempt by pdsc path had a typo (.pds instead of .pdsc).

## Fix

Remove the entry with cpackget rm using the packID without version (for example ARM::SDS) or the exact pdsc path as shown by cpackget list; both worked in the maintainer's test with cpackget 2.2.1 although the pdsc no longer existed. Deleting the pdsc line from local_repository.pidx by hand also works. The maintainers added a note to the documentation and made no tool change.

## Source

Resolution: workaround

Versions: CMSIS-Toolbox 2.14.1, cpackget 2.2.1

From [Open-CMSIS-Pack/cpackget #776](https://github.com/Open-CMSIS-Pack/cpackget/issues/776), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
