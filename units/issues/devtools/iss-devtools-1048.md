---
id: "iss-devtools-1048"
type: "troubleshooting"
domain: "pack"
title: "packchk: packchk from CMSIS-Toolbox 2.0.0 aborts on Ubuntu 20.04"
summary: "The schema validation uses the Xerces library, which converts input through iconv; the glibc behaviour of that path changed between Ubuntu 20.04 and 22.04, so the binary built on the newer system crashes on the older one."
status: "draft"
tool: "packchk"
symptoms: ["packchk: dl-call-libc-early-init.c:37: _dl_call_libc_early_init: Assertion `sym != NULL' failed.", "Aborted"]
symptom_regex: "packchk:\\s+dl\\-call\\-libc\\-early\\-init\\.c:\\S+:\\s+_dl_call_libc_early_init:\\s+Assertion\\s+`sym\\s+!=\\s+NULL'\\s+failed\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1048"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1048"
resolution: "workaround"
versions: "packchk 1.4.1 from cmsis-toolbox 2.0.0 on Ubuntu 20.04"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`packchk: dl-call-libc-early-init.c:37: _dl_call_libc_early_init: Assertion `sym != NULL' failed.`
`Aborted`

## Cause

The schema validation uses the Xerces library, which converts input through iconv; the glibc behaviour of that path changed between Ubuntu 20.04 and 22.04, so the binary built on the newer system crashes on the older one.

## Fix

Run packchk with --disable-validation, which skips the Xerces schema check and lets the remaining checks run. A rebuild of packchk for the older glibc was discussed; the binaries are otherwise intended for newer distributions.

## Source

Resolution: workaround

Versions: packchk 1.4.1 from cmsis-toolbox 2.0.0 on Ubuntu 20.04

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #1048](https://github.com/Open-CMSIS-Pack/devtools/issues/1048), summarized in own words; confidence high, not reviewed yet.
