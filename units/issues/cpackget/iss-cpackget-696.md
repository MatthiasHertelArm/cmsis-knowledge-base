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
resolution: "fixed-in-release"
versions: "fixed after 2.2.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: open <packs>\ARM.CMSIS-Compiler.2.2.0-dev24+g3f9552c\ARM.CMSIS-Compiler.pdsc: The system cannot find the path specified.`

## Cause

cpackget copied the full version including +meta into local_repository.pidx and, on rm without a version, tried to read the missing pdsc to learn the version instead of just matching vendor and pack name.

## Fix

Update to cpackget 2.2.0-4 or later (CMSIS-Toolbox nightly of March 2026): meta information is stripped on add, and rm removes the local_repository entry even when the pdsc file no longer exists.

## Source

Resolution: fixed-in-release

Versions: fixed after 2.2.0

From [Open-CMSIS-Pack/cpackget #696](https://github.com/Open-CMSIS-Pack/cpackget/issues/696), summarized in own words; confidence high, not reviewed yet.
