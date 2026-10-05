---
id: "iss-devtools-166"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuildgen rejects a pack whose pdsc file name differs from the pack name"
summary: "The pdsc file name must be <Vendor>.<Name>.pdsc (packchk reports M207 otherwise); csolution was more lenient than cbuildgen."
status: "draft"
tool: "cbuild"
symptoms: ["*** ERROR M207: <pack root>\\Keil\\ARM_Compiler\\1.6.3\\Keil.ARM_CompilerX.pdsc\n  PDSC file name mismatch!"]
symptom_regex: "<pack\\s+root>\\S+\\\\s+PDSC\\s+file\\s+name\\s+mismatch!"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/166"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/166"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild", "packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M207: <pack root>\Keil\ARM_Compiler\1.6.3\Keil.ARM_CompilerX.pdsc
  PDSC file name mismatch!`

## Cause

The pdsc file name must be <Vendor>.<Name>.pdsc (packchk reports M207 otherwise); csolution was more lenient than cbuildgen.

## Fix

Rename the pdsc to match the pack name. The maintainer believed the tools were aligned by CMSIS-Toolbox 1.1.0 and asked for a test; not confirmed.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #166](https://github.com/Open-CMSIS-Pack/devtools/issues/166), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
