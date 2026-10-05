---
id: "iss-cpackget-56"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget index/update-index fails with 'Access is denied' when index.pidx is read-only"
summary: "Files in the pack root are meant to be read-only."
status: "draft"
tool: "cpackget"
symptoms: ["E: Can't move file \"<packs>\\.Download\\index.pidx\" to \"<packs>\\.Web\\index.pidx\": rename ... Access is denied."]
symptom_regex: "E:\\s+Can't\\s+move\\s+file\\s+\".*?\"\\s+to\\s+\".*?\":\\s+rename\\s+\\.\\.\\.\\s+Access\\s+is\\s+denied\\."
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/56"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/56"
resolution: "workaround"
versions: "MDK 5.36 Pack Installer created the folder"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Can't move file "<packs>\.Download\index.pidx" to "<packs>\.Web\index.pidx": rename ... Access is denied.`

## Cause

Files in the pack root are meant to be read-only. The folder had been set up by MDK's Pack Installer, and cpackget could not overwrite its read-only index.pidx.

## Fix

Remove the read-only attribute from the files in the pack root.

## Source

Resolution: workaround

Versions: MDK 5.36 Pack Installer created the folder

From [Open-CMSIS-Pack/cpackget #56](https://github.com/Open-CMSIS-Pack/cpackget/issues/56), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
