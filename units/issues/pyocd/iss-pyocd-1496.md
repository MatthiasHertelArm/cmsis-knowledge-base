---
id: "iss-pyocd-1496"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd pack install finds no devices; pack update produces XML warnings"
summary: "Updating the index with many concurrent requests triggered server protection at Keil and NXP, leaving corrupted descriptors."
status: "draft"
tool: "pyocd"
symptoms: ["W No matching devices. Please make sure the pack index is up to date. [pack_cmd]"]
symptom_regex: "W\\s+No\\s+matching\\s+devices\\.\\s+Please\\s+make\\s+sure\\s+the\\s+pack\\s+index\\s+is\\s+up\\s+to\\s+date\\."
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1496"
doc_source: "https://github.com/pyocd/pyOCD/issues/1496"
resolution: "fixed-in-release"
versions: "0.34.3"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`W No matching devices. Please make sure the pack index is up to date. [pack_cmd]`

## Cause

Updating the index with many concurrent requests triggered server protection at Keil and NXP, leaving corrupted descriptors.

## Fix

Upgrade cmsis-pack-manager to 0.5.2 or later and run 'pyocd pack update --clean'. Some remaining download errors for broken vendor entries are normal.

## Source

Resolution: fixed-in-release

Versions: 0.34.3

From [pyocd/pyOCD #1496](https://github.com/pyocd/pyOCD/issues/1496), summarized in own words; confidence high, not reviewed yet.
