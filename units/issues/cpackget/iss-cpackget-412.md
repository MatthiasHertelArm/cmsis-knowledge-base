---
id: "iss-cpackget-412"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget download of an NXP pack fails with 404 although curl works"
summary: "The NXP pack server answered 404 to requests with the User-Agent cpackget/v2.1.5, while the same download with a generic Go User-Agent worked; a cpackget change (PR 359) was suspected as the regression."
status: "draft"
tool: "cpackget"
symptoms: ["D: bad status: 404 Not Found", "E: \"https://mcuxpresso.nxp.com/cmsis_pack/repo/NXP.MCXN947_DFP.19.0.0.pack\": bad request"]
symptom_regex: "D:\\s+bad\\s+status:\\s+\\S+\\s+Not\\s+Found"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/412"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/412"
resolution: "fixed-in-release"
versions: "cpackget 2.1.5"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`D: bad status: 404 Not Found`
`E: "https://mcuxpresso.nxp.com/cmsis_pack/repo/NXP.MCXN947_DFP.19.0.0.pack": bad request`

## Cause

The NXP pack server answered 404 to requests with the User-Agent cpackget/v2.1.5, while the same download with a generic Go User-Agent worked; a cpackget change (PR 359) was suspected as the regression.

## Fix

NXP fixed the problem on their side, and the thread's wording ('also fixed') suggests a cpackget change as well without naming it; retry the download.

## Source

Resolution: fixed-in-release

Versions: cpackget 2.1.5

From [Open-CMSIS-Pack/cpackget #412](https://github.com/Open-CMSIS-Pack/cpackget/issues/412), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
