---
id: "iss-cpackget-36"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget list fails in git-bash with 'Pack vendor \"\" does not match' and lists nothing"
summary: "In git-bash/MinGW an unquoted CMSIS_PACK_ROOT or -R value such as C:\\PACKS loses its backslashes (escape characters), yielding a bogus path like C:PACKS."
status: "draft"
tool: "cpackget"
symptoms: ["E: Pack vendor \"\" does not match ^[0-9a-zA-Z_\\-]+$", "E: A pack in the cache folder has malformed pack name: C:.CMSIS_PACKS.ARM.CMSIS-Driver.2.6.1.pack"]
symptom_regex: "E:\\s+Pack\\s+vendor\\s+\".*?\"\\s+does\\s+not\\s+match\\s+\\^\\[\\S+\\-9a\\-zA\\-Z_\\\\\\-\\]\\+\\$"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/36"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/36"
resolution: "user-error"
versions: "0.3.x"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Pack vendor "" does not match ^[0-9a-zA-Z_\-]+$`
`E: A pack in the cache folder has malformed pack name: C:.CMSIS_PACKS.ARM.CMSIS-Driver.2.6.1.pack`

## Cause

In git-bash/MinGW an unquoted CMSIS_PACK_ROOT or -R value such as C:\PACKS loses its backslashes (escape characters), yielding a bogus path like C:PACKS.

## Fix

Quote the path or double the backslashes (export CMSIS_PACK_ROOT='C:\\PACKS'), or use cmd/PowerShell.

## Source

Resolution: user-error

Versions: 0.3.x

From [Open-CMSIS-Pack/cpackget #36](https://github.com/Open-CMSIS-Pack/cpackget/issues/36), summarized in own words; confidence high, not reviewed yet.
