---
id: "iss-pyocd-1817"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Cannot write STM32F1 option bytes: no memory region defined at 0x1ffff800"
summary: "The pack lists the option-byte flash algorithm as non-default, so pyOCD does not create a flash region for it."
status: "draft"
tool: "pyocd"
symptoms: ["no memory region defined for address 0x1ffff800"]
symptom_regex: "no\\s+memory\\s+region\\s+defined\\s+for\\s+address\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1817"
doc_source: "https://github.com/pyocd/pyOCD/issues/1817"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["STM32F103C6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`no memory region defined for address 0x1ffff800`

## Cause

The pack lists the option-byte flash algorithm as non-default, so pyOCD does not create a flash region for it.

## Fix

Add the region yourself in a pyocd_user.py script: load the unprocessed pack algorithms and add a FlashRegion for the option-byte algorithm to the memory map.

## Source

Resolution: workaround

From [pyocd/pyOCD #1817](https://github.com/pyocd/pyOCD/issues/1817), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
