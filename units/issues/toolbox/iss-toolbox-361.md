---
id: "iss-toolbox-361"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution 2.9.0 stops with \"no default rwx memory\" for a device pack"
summary: "The device pack description was invalid (schema errors such as wrong Dvendor, element order and unsupported characters in descriptions); the newer csolution is stricter and cannot derive memory."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: no default rwx memory nor algorithm with ramstart/size was found"]
symptom_regex: "no\\s+default\\s+rwx\\s+memory\\s+nor\\s+algorithm\\s+with\\s+ramstart/size\\s+was\\s+found"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/361"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/361"
resolution: "user-error"
versions: "worked in 2.8.0, failed in 2.9.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: no default rwx memory nor algorithm with ramstart/size was found`

## Cause

The device pack description was invalid (schema errors such as wrong Dvendor, element order and unsupported characters in descriptions); the newer csolution is stricter and cannot derive memory.

## Fix

Run packchk on the pack, fix the schema errors and memory/algorithm definitions, then rebuild.

## Source

Resolution: user-error

Versions: worked in 2.8.0, failed in 2.9.0

From [Open-CMSIS-Pack/cmsis-toolbox #361](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/361), summarized in own words; confidence high, not reviewed yet.
