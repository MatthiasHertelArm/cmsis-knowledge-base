---
id: "iss-cpackget-174"
type: "troubleshooting"
domain: "pack"
title: "cpackget: Two different default pack folders on macOS (gen-pack vs cpackget)"
summary: "gen-pack looked in a different default than cpackget; the default is ~/.cache/arm/packs (all lower case, with a dot) on macOS and Linux, and XDG_CACHE_HOME is honoured by cpackget."
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/174"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/174"
resolution: "configuration"
versions: "2023"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

gen-pack looked in a different default than cpackget; the default is ~/.cache/arm/packs (all lower case, with a dot) on macOS and Linux, and XDG_CACHE_HOME is honoured by cpackget.

## Fix

Set CMSIS_PACK_ROOT explicitly, or remove the stray differently-cased folder and let cpackget recreate ~/.cache/arm/packs.

## Source

Resolution: configuration

Versions: 2023

From [Open-CMSIS-Pack/cpackget #174](https://github.com/Open-CMSIS-Pack/cpackget/issues/174), summarized in own words; confidence medium, not reviewed yet.
