---
id: "iss-pyocd-2023"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flash load after halting a running target fails with IPSR=3 or flash init timeout"
summary: "Flash algorithms typically assume the device has been reset before they run; loading after only halting a running application is not supported, and the algorithm then faults or times out."
status: "draft"
tool: "pyocd"
symptoms: ["target was not halted as expected after calling flash algorithm routine (IPSR=3)", "flash init timed out"]
symptom_regex: "target\\s+was\\s+not\\s+halted\\s+as\\s+expected\\s+after\\s+calling\\s+flash\\s+algorithm\\s+routine\\s+\\(IPSR=\\S+\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2023"
doc_source: "https://github.com/pyocd/pyOCD/issues/2023"
resolution: "configuration"
versions: "0.45.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`target was not halted as expected after calling flash algorithm routine (IPSR=3)`
`flash init timed out`

## Cause

Flash algorithms typically assume the device has been reset before they run; loading after only halting a running application is not supported, and the algorithm then faults or times out.

## Fix

Reset the target and halt it before programming: use 'reset halt' in the commander, or 'monitor reset halt' before 'load' in gdb. 'pyocd flash' already does this by default.

## Source

Resolution: configuration

Versions: 0.45.0

From [pyocd/pyOCD #2023](https://github.com/pyocd/pyOCD/issues/2023), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
