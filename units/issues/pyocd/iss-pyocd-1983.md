---
id: "iss-pyocd-1983"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: fast_program with smart_flash leaves parts of erased sectors blank (silent data loss)"
summary: "With fast_program and smart_flash, pages whose CRC matched were marked unchanged and the step that forces all pages of a dirty sector to be rewritten was skipped."
status: "draft"
tool: "pyocd"
symptoms: ["Erased 32768 bytes (2 sectors), programmed 8192 bytes (2 pages), skipped 57344 bytes (14 pages)"]
symptom_regex: "Erased\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+sectors\\),\\s+programmed\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+pages\\),\\s+skipped\\s+\\S+\\s+bytes\\s+\\(\\S+\\s+pages\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1983"
doc_source: "https://github.com/pyocd/pyOCD/issues/1983"
resolution: "fixed-in-release"
versions: "seen on 0.44.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "family": ["STM32F4 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Erased 32768 bytes (2 sectors), programmed 8192 bytes (2 pages), skipped 57344 bytes (14 pages)`

## Cause

With fast_program and smart_flash, pages whose CRC matched were marked unchanged and the step that forces all pages of a dirty sector to be rewritten was skipped. Sector erase then wiped pages that were never reprogrammed, on devices whose sectors are larger than pages.

## Fix

Update pyOCD to a release including change #2004. Until then avoid -O fast_program=true together with smart_flash on parts with sector size larger than page size, and verify read-back.

## Source

Resolution: fixed-in-release

Versions: seen on 0.44.1

From [pyocd/pyOCD #1983](https://github.com/pyocd/pyOCD/issues/1983), summarized in own words; confidence high, checked against the thread, not reviewed yet.
