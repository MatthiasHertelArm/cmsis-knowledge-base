---
id: "iss-pyocd-848"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: flash script fails: 'MemoryMap' object has no attribute 'get_region_by_name'"
summary: "get_region_by_name() was removed from MemoryMap after 0.24 in favour of a general lookup; the user-script example still used the old name."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: 'MemoryMap' object has no attribute 'get_region_by_name'"]
symptom_regex: "uncaught\\s+exception:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/848"
doc_source: "https://github.com/pyocd/pyOCD/issues/848"
resolution: "not-a-bug"
versions: "0.24 and later"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: 'MemoryMap' object has no attribute 'get_region_by_name'`

## Cause

get_region_by_name() was removed from MemoryMap after 0.24 in favour of a general lookup; the user-script example still used the old name.

## Fix

Use target.memory_map.get_first_matching_region(name="flexspi") (keyword arguments match any region attribute); the documentation example was fixed in #849.

## Source

Resolution: not-a-bug

Versions: 0.24 and later

From [pyocd/pyOCD #848](https://github.com/pyocd/pyOCD/issues/848), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
