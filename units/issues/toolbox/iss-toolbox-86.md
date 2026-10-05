---
id: "iss-toolbox-86"
type: "troubleshooting"
domain: "pack"
title: "packchk: packchk M511: processor element not allowed inside subFamily"
summary: "The pack schema is order sensitive: processor must come before description in the subFamily body."
status: "draft"
tool: "packchk"
symptoms: ["Xerxes reports: element 'processor' is not allowed for content model '(deprecated?,processor*,debugconfig?,"]
symptom_regex: "Xerxes\\s+reports:\\s+element\\s+'.*?'\\s+is\\s+not\\s+allowed\\s+for\\s+content\\s+model\\s+'\\(deprecated\\?,processor\\*,debugconfig\\?,"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/86"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/86"
resolution: "user-error"
versions: "packchk 1.4.1"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Xerxes reports: element 'processor' is not allowed for content model '(deprecated?,processor*,debugconfig?,`

## Cause

The pack schema is order sensitive: processor must come before description in the subFamily body.

## Fix

Move the processor element to the start of the subFamily; use an XML editor with schema validation. A schema PR to relax the order was opened.

## Source

Resolution: user-error

Versions: packchk 1.4.1

From [Open-CMSIS-Pack/cmsis-toolbox #86](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/86), summarized in own words; confidence high, checked against the thread, not reviewed yet.
