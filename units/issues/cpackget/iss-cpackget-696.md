---
id: "iss-cpackget-696"
type: "troubleshooting"
domain: "pack"
title: "cpackget: Local pack with +build version keeps metadata; rm fails when pdsc is gone"
summary: "cpackget copied the full version including +meta into local_repository.pidx and, on rm without a version, tried to read the missing pdsc to learn the version instead of just matching vendor and pack name."
status: "draft"
tool: "cpackget"
symptoms: ["E: open <packs>\\ARM.CMSIS-Compiler.2.2.0-dev24+g3f9552c\\ARM.CMSIS-Compiler.pdsc: The system cannot find the path specified."]
symptom_regex: "E:\\s+open\\s+<packs>\\S+:\\s+The\\s+system\\s+cannot\\s+find\\s+the\\s+path\\s+specified\\."
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/696"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/696"
resolution: "workaround"
versions: "affected up to cpackget 2.2.0; validated with 2.2.0-4-g487974c"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: open <packs>\ARM.CMSIS-Compiler.2.2.0-dev24+g3f9552c\ARM.CMSIS-Compiler.pdsc: The system cannot find the path specified.`

## Cause

cpackget copied the full version including +meta into local_repository.pidx and, on rm without a version, tried to read the missing pdsc to learn the version instead of just matching vendor and pack name.

## Fix

Use a cpackget newer than 2.2.0 with the change (validated with build 2.2.0-4-g487974c): meta information is stripped on add, and rm removes the local_repository entry even when the pdsc file no longer exists. Otherwise remove the entry from local_repository.pidx by hand or put the pdsc file back.

## Source

Resolution: workaround

Versions: affected up to cpackget 2.2.0; validated with 2.2.0-4-g487974c

From [Open-CMSIS-Pack/cpackget #696](https://github.com/Open-CMSIS-Pack/cpackget/issues/696), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
