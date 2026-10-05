---
id: "iss-pyocd-1232"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyyaml version conflict between pyocd and cmsis-pack-manager"
summary: "pyOCD pinned pyyaml below 6.0 while newer cmsis-pack-manager required 6.0."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR: cmsis-pack-manager 0.4.0 has requirement pyyaml<7.0,>=6.0, but you'll have pyyaml 5.4.1 which is incompatible."]
symptom_regex: "cmsis\\-pack\\-manager\\s+\\S+\\s+has\\s+requirement\\s+pyyaml<\\S+,>=\\S+,\\s+but\\s+you'll\\s+have\\s+pyyaml\\s+\\S+\\s+which\\s+is\\s+incompatible\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1232"
doc_source: "https://github.com/pyocd/pyOCD/issues/1232"
resolution: "fixed-in-release"
versions: "fixed 0.32.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR: cmsis-pack-manager 0.4.0 has requirement pyyaml<7.0,>=6.0, but you'll have pyyaml 5.4.1 which is incompatible.`

## Cause

pyOCD pinned pyyaml below 6.0 while newer cmsis-pack-manager required 6.0.

## Fix

Upgrade to pyOCD 0.32.1.

## Source

Resolution: fixed-in-release

Versions: fixed 0.32.1

From [pyocd/pyOCD #1232](https://github.com/pyocd/pyOCD/issues/1232), summarized in own words; confidence high, checked against the thread, not reviewed yet.
