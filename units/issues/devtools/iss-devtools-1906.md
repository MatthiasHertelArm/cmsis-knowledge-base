---
id: "iss-devtools-1906"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add fails to download a pack from a server that sets cookies"
summary: "The pack server redirects through a JavaScript page and only serves the file after it has set a cookie, so a client without cookie handling never gets the pack although a browser does."
status: "draft"
tool: "cpackget"
symptoms: ["E: \"https://www.geehy.com/uploads/tool/Geehy.APM32A0xx_DFP.1.0.0.pack\": failed to download file"]
symptom_regex: "E:\\s+\".*?\":\\s+failed\\s+to\\s+download\\s+file"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1906"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1906"
resolution: "fixed-in-release"
versions: "2.1.4, fixed in 2.1.5"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: "https://www.geehy.com/uploads/tool/Geehy.APM32A0xx_DFP.1.0.0.pack": failed to download file`

## Cause

The pack server redirects through a JavaScript page and only serves the file after it has set a cookie, so a client without cookie handling never gets the pack although a browser does.

## Fix

Fixed by cookie support in cpackget (2.1.5 line, seen in 2.1.5-6). Update the toolbox. A failed cbuild setup also should no longer overwrite an existing cbuild-run.yml.

## Source

Resolution: fixed-in-release

Versions: 2.1.4, fixed in 2.1.5

From [Open-CMSIS-Pack/devtools #1906](https://github.com/Open-CMSIS-Pack/devtools/issues/1906), summarized in own words; confidence high, not reviewed yet.
