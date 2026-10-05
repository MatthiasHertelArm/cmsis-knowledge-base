---
id: "iss-cpackget-511"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add fails with 'zip: not a valid zip file' (corrupt cached pack)"
summary: "The cached file in .Download is incomplete or corrupted (interrupted or failed download, sometimes 0 bytes) and cpackget reuses the cache."
status: "draft"
tool: "cpackget"
symptoms: ["E: Can't decompress \"<packs>/.Download/ARM.CMSIS.6.1.0.pack\": zip: not a valid zip file", "E: fail to decompress file"]
symptom_regex: "E:\\s+Can't\\s+decompress\\s+\".*?\":\\s+zip:\\s+not\\s+a\\s+valid\\s+zip\\s+file"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/511"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/511"
resolution: "workaround"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Can't decompress "<packs>/.Download/ARM.CMSIS.6.1.0.pack": zip: not a valid zip file`
`E: fail to decompress file`

## Cause

The cached file in .Download is incomplete or corrupted (interrupted or failed download, sometimes 0 bytes) and cpackget reuses the cache.

## Fix

Remove the bad cache entry with cpackget rm --purge ARM::CMSIS@6.1.0 (or delete the file in .Download) and run cpackget add again; if it recurs run with -v and check the network/proxy.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cpackget #511](https://github.com/Open-CMSIS-Pack/cpackget/issues/511), summarized in own words; confidence high, not reviewed yet.
