---
id: "iss-cpackget-511"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add fails with 'zip: not a valid zip file' (corrupt cached pack)"
summary: "The pack file cached in .Download was damaged by a failed download, and cpackget used that cached file."
status: "draft"
tool: "cpackget"
symptoms: ["E: Can't decompress \"<packs>/.Download/ARM.CMSIS.6.1.0.pack\": zip: not a valid zip file", "E: fail to decompress file"]
symptom_regex: "E:\\s+Can't\\s+decompress\\s+\".*?\":\\s+zip:\\s+not\\s+a\\s+valid\\s+zip\\s+file"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/511"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/511"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Can't decompress "<packs>/.Download/ARM.CMSIS.6.1.0.pack": zip: not a valid zip file`
`E: fail to decompress file`

## Cause

The pack file cached in .Download was damaged by a failed download, and cpackget used that cached file.

## Fix

Run cpackget rm --purge ARM::CMSIS@6.1.0 to drop the cached pack, then cpackget add ARM::CMSIS@6.1.0 again; if it still fails, rerun with -v to get a log.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cpackget #511](https://github.com/Open-CMSIS-Pack/cpackget/issues/511), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
