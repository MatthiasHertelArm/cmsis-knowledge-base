---
id: "iss-devtools-1900"
type: "troubleshooting"
domain: "project"
title: "csolution: unexpected instance type for empty variables: node, then cbuild-pack.yml not written"
summary: "A variables: node in a target-type had no valid - variable: entries (all items were commented out), so the YAML is invalid; the second error line was only a follow-up with an empty path."
status: "draft"
tool: "csolution"
symptoms: ["C:/w/AWS_MQTT_Demo/Demo.csolution.yml:43:7 - error csolution: unexpected instance type", "/.cbuild-pack.yml - error csolution: file cannot be written"]
symptom_regex: "unexpected\\s+instance\\s+type"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1900"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1900"
resolution: "user-error"
versions: "2.6.x"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C:/w/AWS_MQTT_Demo/Demo.csolution.yml:43:7 - error csolution: unexpected instance type`
`/.cbuild-pack.yml - error csolution: file cannot be written`

## Cause

A variables: node in a target-type had no valid - variable: entries (all items were commented out), so the YAML is invalid; the second error line was only a follow-up with an empty path.

## Fix

Remove the empty variables: node or give it at least one list entry. Later toolbox builds no longer print the misleading second error.

## Source

Resolution: user-error

Versions: 2.6.x

From [Open-CMSIS-Pack/devtools #1900](https://github.com/Open-CMSIS-Pack/devtools/issues/1900), summarized in own words; confidence high, not reviewed yet.
