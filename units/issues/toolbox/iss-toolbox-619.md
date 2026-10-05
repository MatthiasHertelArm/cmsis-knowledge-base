---
id: "iss-toolbox-619"
type: "troubleshooting"
domain: "project"
title: "csolution: \"board not found\" from csolution run -g when an unselected project lists a missing pack"
summary: "Running a generator creates cbuild-gen files for every project context sharing the build and target type, so packs listed by projects outside the active target set must be installed too."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: board 'STM32H743I-EVAL:Rev.B' was not found"]
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/619"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/619"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "family": ["STM32H7 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: board 'STM32H743I-EVAL:Rev.B' was not found`

## Cause

Running a generator creates cbuild-gen files for every project context sharing the build and target type, so packs listed by projects outside the active target set must be installed too. When one is missing the tool reports a misleading board or device error instead of the missing pack.

## Fix

List the missing packs with csolution list packs <solution> -c *.<build>+<target> -m and install them. The fix passes the active target (-a <target>) when launching the generator so only the selected projects are processed; available from the August 2026 nightly and the matching extension build.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cmsis-toolbox #619](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/619), summarized in own words; confidence high, not reviewed yet.
