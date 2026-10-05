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
versions: "cpackget 2.2.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Pack "arm::sds@3.0.0-dev" is not installed`
`E: pack not installed`

## Cause

A pack registered via its pdsc file stays in .Local/local_repository.pidx after the pdsc is deleted. The rm attempt in the report used a name that did not match the entry (and a pdsc path with a typo), hence the refusal.

## Fix

Remove the entry with cpackget rm using the exact packID (vendor::name, optionally with the version) or the exact pdsc path as shown by cpackget list; if that still fails, delete the matching pdsc line from <CMSIS_PACK_ROOT>/.Local/local_repository.pidx by hand. The maintainers documented this and made no tool change.

## Source

Resolution: workaround

Versions: cpackget 2.2.1

From [Open-CMSIS-Pack/cpackget #776](https://github.com/Open-CMSIS-Pack/cpackget/issues/776), summarized in own words; confidence medium, not reviewed yet.
