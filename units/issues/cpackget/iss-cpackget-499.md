---
id: "iss-cpackget-499"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add fails because pack IDs were matched case-sensitively"
summary: "Pack ID lookup compared vendor and pack names case-sensitively, but the pack is published as Arm.ethos-u-core-driver while projects reference ARM::ethos-u-core-driver."
status: "draft"
tool: "cpackget"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/499"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/499"
resolution: "fixed-in-release"
versions: "2.1.6 affected"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Pack ID lookup compared vendor and pack names case-sensitively, but the pack is published as Arm.ethos-u-core-driver while projects reference ARM::ethos-u-core-driver.

## Fix

Use CMSIS-Toolbox nightly 2025-04-10 or later (cpackget 2.1.7+), which searches pack IDs case-insensitively.

## Source

Resolution: fixed-in-release

Versions: 2.1.6 affected

From [Open-CMSIS-Pack/cpackget #499](https://github.com/Open-CMSIS-Pack/cpackget/issues/499), summarized in own words; confidence high, not reviewed yet.
