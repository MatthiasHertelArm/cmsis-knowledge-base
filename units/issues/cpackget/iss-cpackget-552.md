---
id: "iss-cpackget-552"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add reports 'pdsc not found' inside a freshly downloaded pack"
summary: "The .Web folder still held an old pdsc of the pack, which was no longer being updated, so the pack lookup and the downloaded pack disagreed."
status: "draft"
tool: "cpackget"
symptoms: ["E: \"ARM.ethos-u-core-driver.pdsc\" not found in \"<packs>\\.Download\\Arm.ethos-u-core-driver.1.24.11.pack\"", "E: pdsc not found"]
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/552"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/552"
resolution: "fixed-in-release"
versions: "cpackget 2.1.8; fixed in a later nightly"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: "ARM.ethos-u-core-driver.pdsc" not found in "<packs>\.Download\Arm.ethos-u-core-driver.1.24.11.pack"`
`E: pdsc not found`

## Cause

The .Web folder still held an old pdsc of the pack, which was no longer being updated, so the pack lookup and the downloaded pack disagreed.

## Fix

Remove the stale <vendor>.<name>.pdsc from .Web (or run cpackget update-index) and add again; the maintainers verified a fix in a later nightly.

## Source

Resolution: fixed-in-release

Versions: cpackget 2.1.8; fixed in a later nightly

From [Open-CMSIS-Pack/cpackget #552](https://github.com/Open-CMSIS-Pack/cpackget/issues/552), summarized in own words; confidence medium, not reviewed yet.
