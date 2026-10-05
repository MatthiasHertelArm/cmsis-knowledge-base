---
id: "iss-cpackget-412"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget download of an NXP pack fails with 404 although curl works"
summary: "The pack server rejected requests that carried cpackget's own User-Agent string (introduced in 2.1.5), while a generic Go User-Agent worked."
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
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`D: bad status: 404 Not Found`
`E: "https://mcuxpresso.nxp.com/cmsis_pack/repo/NXP.MCXN947_DFP.19.0.0.pack": bad request`

## Cause

The pack server rejected requests that carried cpackget's own User-Agent string (introduced in 2.1.5), while a generic Go User-Agent worked.

## Fix

The server-side rule was corrected by the vendor; retry the download. No change on the client was needed.

## Source

Resolution: fixed-in-release

Versions: cpackget 2.1.5

From [Open-CMSIS-Pack/cpackget #412](https://github.com/Open-CMSIS-Pack/cpackget/issues/412), summarized in own words; confidence medium, not reviewed yet.
