---
id: "iss-cpackget-552"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add reports 'pdsc not found' inside a freshly downloaded pack"
summary: "An old pdsc of the pack in the .Web folder was no longer being updated, so cpackget did not find the expected pdsc in the downloaded pack."
status: "draft"
tool: "cpackget"
symptoms: ["E: \"ARM.ethos-u-core-driver.pdsc\" not found in \"<packs>\\.Download\\Arm.ethos-u-core-driver.1.24.11.pack\"", "E: pdsc not found"]
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/552"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/552"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: "ARM.ethos-u-core-driver.pdsc" not found in "<packs>\.Download\Arm.ethos-u-core-driver.1.24.11.pack"`
`E: pdsc not found`

## Cause

An old pdsc of the pack in the .Web folder was no longer being updated, so cpackget did not find the expected pdsc in the downloaded pack.

## Fix

Delete the outdated pdsc of that pack from .Web and add the pack again; the issue was later marked verified without naming a release.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cpackget #552](https://github.com/Open-CMSIS-Pack/cpackget/issues/552), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
