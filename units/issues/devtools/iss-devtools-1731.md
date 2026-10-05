---
id: "iss-devtools-1731"
type: "troubleshooting"
domain: "project"
title: "cbuild: CMake error about invalid target name when a context name contains a blank"
summary: "Project, build-type and target-type names form the context name, which becomes a CMake target name; blanks and other characters CMake restricts are not allowed."
status: "draft"
tool: "cbuild"
symptoms: ["The target name \"Hello.Debug+AVH Test\" is reserved or not valid for certain CMake features, such as generator expressions, and may result in undefined behavior."]
symptom_regex: "The\\s+target\\s+name\\s+\".*?\"\\s+is\\s+reserved\\s+or\\s+not\\s+valid\\s+for\\s+certain\\s+CMake\\s+features,\\s+such\\s+as\\s+generator\\s+expressions,\\s+and\\s+may\\s+result\\s+in\\s+undefined\\s+behavior\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1731"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1731"
resolution: "user-error"
versions: "2.5.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`The target name "Hello.Debug+AVH Test" is reserved or not valid for certain CMake features, such as generator expressions, and may result in undefined behavior.`

## Cause

Project, build-type and target-type names form the context name, which becomes a CMake target name; blanks and other characters CMake restricts are not allowed.

## Fix

Use names without blanks (underscore or dash instead). The restriction was added to the toolbox documentation.

## Source

Resolution: user-error

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1731](https://github.com/Open-CMSIS-Pack/devtools/issues/1731), summarized in own words; confidence high, checked against the thread, not reviewed yet.
