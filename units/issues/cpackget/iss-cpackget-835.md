---
id: "iss-cpackget-835"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add crashes (nil pointer) with a locally generated index.pidx"
summary: "vidx2pidx wrote the index file name into the url element (file:///.../index.pidx), so cpackget built a doubled path index.pidx/index.pidx and then dereferenced a missing file info instead of reporting an error."
status: "draft"
tool: "cpackget"
symptoms: ["runtime error: invalid memory address or nil pointer dereference"]
symptom_regex: "runtime\\s+error:\\s+invalid\\s+memory\\s+address\\s+or\\s+nil\\s+pointer\\s+dereference"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/835"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/835"
resolution: "fixed-in-release"
versions: "fixed in CMSIS-Toolbox nightly 2026-09-16"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cpackget", "vidx2pidx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`runtime error: invalid memory address or nil pointer dereference`

## Cause

vidx2pidx wrote the index file name into the url element (file:///.../index.pidx), so cpackget built a doubled path index.pidx/index.pidx and then dereferenced a missing file info instead of reporting an error.

## Fix

Use a CMSIS-Toolbox nightly from 2026-09-16 or later, where both vidx2pidx and cpackget are fixed; the url element of a local index must name only the folder (file:///C:/packs/Vendor/). As a workaround place an update.cfg in .Web with a future Date and Auto=false to suppress the implicit update-index.

## Source

Resolution: fixed-in-release

Versions: fixed in CMSIS-Toolbox nightly 2026-09-16

From [Open-CMSIS-Pack/cpackget #835](https://github.com/Open-CMSIS-Pack/cpackget/issues/835), summarized in own words; confidence high, checked against the thread, not reviewed yet.
