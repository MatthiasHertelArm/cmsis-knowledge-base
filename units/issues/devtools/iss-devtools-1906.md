---
id: "iss-devtools-1906"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add fails to download a pack from a server that sets cookies"
summary: "The pack server answers a plain client with a JavaScript redirect page and serves the file only once a cookie has been set, so a client without cookie handling never gets the pack although a browser does."
status: "draft"
tool: "cpackget"
symptoms: ["E: \"https://www.geehy.com/uploads/tool/Geehy.APM32A0xx_DFP.1.0.0.pack\": failed to download file"]
symptom_regex: "E:\\s+\".*?\":\\s+failed\\s+to\\s+download\\s+file"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1906"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1906"
resolution: "fixed-in-release"
versions: "cpackget 2.1.4-46-g97fca47 affected; fix seen in 2.1.5-6-gd958da1 (toolbox nightly 2.6.1-38)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: "https://www.geehy.com/uploads/tool/Geehy.APM32A0xx_DFP.1.0.0.pack": failed to download file`

## Cause

The pack server answers a plain client with a JavaScript redirect page and serves the file only once a cookie has been set, so a client without cookie handling never gets the pack although a browser does.

## Fix

Fixed by cookie support in cpackget, seen in cpackget 2.1.5-6-gd958da1 from the CMSIS-Toolbox nightly 2.6.1-38; update the toolbox. In that nightly a failed cbuild setup also no longer writes cbuild-run.yml.

## Source

Resolution: fixed-in-release

Versions: cpackget 2.1.4-46-g97fca47 affected; fix seen in 2.1.5-6-gd958da1 (toolbox nightly 2.6.1-38)

From [Open-CMSIS-Pack/devtools #1906](https://github.com/Open-CMSIS-Pack/devtools/issues/1906), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
