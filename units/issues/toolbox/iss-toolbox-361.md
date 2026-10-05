---
id: "iss-toolbox-361"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution 2.9.0 stops with \"no default rwx memory\" for a device pack"
summary: "The device pack description had many errors reported by packchk (schema errors such as the Dvendor value, the element order in <devices>, unsupported characters in descriptions and an invalid startup attribute on <algorithm>); csolution 2.9.0 reported the error for …"
status: "draft"
tool: "csolution"
symptoms: ["error csolution: no default rwx memory nor algorithm with ramstart/size was found"]
symptom_regex: "no\\s+default\\s+rwx\\s+memory\\s+nor\\s+algorithm\\s+with\\s+ramstart/size\\s+was\\s+found"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/361"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/361"
resolution: "user-error"
versions: "CMSIS-Toolbox 2.8.0 works, 2.9.0 fails; packchk 1.4.3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: no default rwx memory nor algorithm with ramstart/size was found`

## Cause

The device pack description had many errors reported by packchk (schema errors such as the Dvendor value, the element order in <devices>, unsupported characters in descriptions and an invalid startup attribute on <algorithm>); csolution 2.9.0 reported the error for it while 2.8.0 built the project.

## Fix

Run packchk on the pack and fix the reported errors in the pdsc; the reporter then said the problem was solved.

## Source

Resolution: user-error

Versions: CMSIS-Toolbox 2.8.0 works, 2.9.0 fails; packchk 1.4.3

From [Open-CMSIS-Pack/cmsis-toolbox #361](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/361), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
