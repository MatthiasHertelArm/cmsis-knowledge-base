---
id: "iss-dbg-942"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd load says \"Invalid .cbuild-run.yml file\" when given a .cbuild.yml file"
summary: "The --cbuild-run option was pointed at the cbuild.yml build description instead of the generated *.cbuild-run.yml, and the message did not say what was wrong."
status: "draft"
tool: "pyocd"
symptoms: ["0000732 C Invalid .cbuild-run.yml file '<project>/out/App/App.cbuild.yml' [__main__]"]
symptom_regex: "Invalid\\s+\\.cbuild\\-run\\.yml\\s+file\\s+'.*?'"
collection: "issues-dbg"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/942"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/942"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`0000732 C Invalid .cbuild-run.yml file '<project>/out/App/App.cbuild.yml' [__main__]`

## Cause

The --cbuild-run option was pointed at the cbuild.yml build description instead of the generated *.cbuild-run.yml, and the message did not say what was wrong.

## Fix

Pass the file ending in .cbuild-run.yml. A clearer error message was implemented in pyOCD PR 2003; no release is named.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/vscode-cmsis-debugger #942](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/issues/942), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
