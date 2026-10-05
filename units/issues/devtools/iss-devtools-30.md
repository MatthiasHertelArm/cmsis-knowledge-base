---
id: "iss-devtools-30"
type: "troubleshooting"
domain: "project"
title: "cbuild: ERROR M800 R821 Required pack not installed for a pack registered in local_repository.pidx"
summary: "Locally referenced packs were not supported by the early build tools."
status: "draft"
tool: "cbuild"
symptoms: ["*** ERROR M800:\n  RTE Model reports: Error R821: Required pack not installed"]
symptom_regex: "RTE\\s+Model\\s+reports:\\s+Error\\s+R821:\\s+Required\\s+pack\\s+not\\s+installed"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/30"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/30"
resolution: "fixed-in-release"
versions: "2021"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M800:
  RTE Model reports: Error R821: Required pack not installed`

## Cause

Locally referenced packs were not supported by the early build tools.

## Fix

Support was added shortly after the report (devtools PR 33); use a current CMSIS-Toolbox.

## Source

Resolution: fixed-in-release

Versions: 2021

From [Open-CMSIS-Pack/devtools #30](https://github.com/Open-CMSIS-Pack/devtools/issues/30), summarized in own words; confidence high, not reviewed yet.
