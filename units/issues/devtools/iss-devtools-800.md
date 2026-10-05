---
id: "iss-devtools-800"
type: "troubleshooting"
domain: "pack"
title: "packchk: ERROR M313 Associated File/Path is outside PACK root when pack paths contain ./"
summary: "packchk compares the canonical file path against the pack root with a plain string prefix check; a PDSC location containing ./ segments prevents the match, so valid files look outside the pack."
status: "draft"
tool: "packchk"
symptoms: ["*** ERROR M313: <pack>/./cmsis-pack/.build/<vendor>.<name>.pdsc (Line 30) \n  Associated File/Path is outside PACK root: 'src/include/lwfsm/'"]
symptom_regex: "<pack>\\S+<vendor>\\.<name>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\s+\\\\s+Associated\\s+File/Path\\s+is\\s+outside\\s+PACK\\s+root:\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/800"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/800"
resolution: "workaround"
versions: "packchk 1.3.98"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M313: <pack>/./cmsis-pack/.build/<vendor>.<name>.pdsc (Line 30) 
  Associated File/Path is outside PACK root: 'src/include/lwfsm/'`

## Cause

packchk compares the canonical file path against the pack root with a plain string prefix check; a PDSC location containing ./ segments prevents the match, so valid files look outside the pack.

## Fix

Run packchk on a pdsc whose path has no ./ or ../ segments (call the script with a normalized absolute path). A fix normalizing the paths was proposed in the thread.

## Source

Resolution: workaround

Versions: packchk 1.3.98

From [Open-CMSIS-Pack/devtools #800](https://github.com/Open-CMSIS-Pack/devtools/issues/800), summarized in own words; confidence low, not reviewed yet.
