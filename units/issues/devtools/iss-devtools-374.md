---
id: "iss-devtools-374"
type: "troubleshooting"
domain: "project"
title: "cbuild: Local pack version read from the pidx instead of the pdsc; cbuild asks for a pack"
summary: "cbuildgen read the version of a locally referenced pack from the local_repository.pidx entry, which becomes stale when the pdsc version changes."
status: "draft"
tool: "cbuild"
symptoms: ["error cbuild: cpackget was not found, missing packs cannot be downloaded", "info cbuild: missing packs must be installed, rerun cbuild with the --packs option"]
symptom_regex: "cpackget\\s+was\\s+not\\s+found,\\s+missing\\s+packs\\s+cannot\\s+be\\s+downloaded"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/374"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/374"
resolution: "workaround"
versions: "cbuild 0.9.1 / cbuildgen 0.11.2, still seen in 1.0.0; fixes offered in 1.1.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error cbuild: cpackget was not found, missing packs cannot be downloaded`
`info cbuild: missing packs must be installed, rerun cbuild with the --packs option`

## Cause

cbuildgen read the version of a locally referenced pack from the local_repository.pidx entry, which becomes stale when the pdsc version changes.

## Fix

Workaround: update the version in local_repository.pidx to match the pdsc. Fixes for cbuildgen packlist (PR #442) and the exit code (cbuild PR #9) were offered for testing in CMSIS-Toolbox 1.1.0, not confirmed in the thread.

## Source

Resolution: workaround

Versions: cbuild 0.9.1 / cbuildgen 0.11.2, still seen in 1.0.0; fixes offered in 1.1.0

From [Open-CMSIS-Pack/devtools #374](https://github.com/Open-CMSIS-Pack/devtools/issues/374), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
