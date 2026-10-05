---
id: "iss-cpackget-36"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget list fails in git-bash with 'Pack vendor \"\" does not match' and lists nothing"
summary: "In git-bash/MinGW a CMSIS_PACK_ROOT such as /c/CMSIS_PACKS reaches cpackget as C:/CMSIS_PACKS with forward slashes, and cpackget list then fails to parse the installed pack paths."
status: "draft"
tool: "cpackget"
symptoms: ["E: Pack vendor \"\" does not match ^[0-9a-zA-Z_\\-]+$", "E: A pack in the cache folder has malformed pack name: C:.CMSIS_PACKS.ARM.CMSIS-Driver.2.6.1.pack"]
symptom_regex: "E:\\s+Pack\\s+vendor\\s+\".*?\"\\s+does\\s+not\\s+match\\s+\\^\\[\\S+\\-9a\\-zA\\-Z_\\\\\\-\\]\\+\\$"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/36"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/36"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Pack vendor "" does not match ^[0-9a-zA-Z_\-]+$`
`E: A pack in the cache folder has malformed pack name: C:.CMSIS_PACKS.ARM.CMSIS-Driver.2.6.1.pack`

## Cause

In git-bash/MinGW a CMSIS_PACK_ROOT such as /c/CMSIS_PACKS reaches cpackget as C:/CMSIS_PACKS with forward slashes, and cpackget list then fails to parse the installed pack paths. An unquoted C:\PACKS in export or -R also loses its backslashes, which bash treats as escape characters, and becomes C:PACKS.

## Fix

Set the pack root with doubled backslashes (export CMSIS_PACK_ROOT=c:\\CMSIS_PACKS) or quote it (cpackget -R "C:\PACKS").

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cpackget #36](https://github.com/Open-CMSIS-Pack/cpackget/issues/36), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
