---
id: "iss-pyocd-969"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd commander --elf crashes with 'name os is not defined'"
summary: "Regression in commands/commander.py: the os module is not imported and self.target.elf should be self.session.target.elf, so --elf crashes."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: name 'os' is not defined"]
symptom_regex: "uncaught\\s+exception:\\s+name\\s+'.*?'\\s+is\\s+not\\s+defined"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/969"
doc_source: "https://github.com/pyocd/pyOCD/issues/969"
resolution: "workaround"
versions: "0.28.1.dev6"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: name 'os' is not defined`

## Cause

Regression in commands/commander.py: the os module is not imported and self.target.elf should be self.session.target.elf, so --elf crashes.

## Fix

Apply the reporter's patch (import os, use self.session.target.elf); the maintainer said he would ship a fix with it shortly.

## Source

Resolution: workaround

Versions: 0.28.1.dev6

From [pyocd/pyOCD #969](https://github.com/pyocd/pyOCD/issues/969), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
