---
id: "iss-sol-550"
type: "troubleshooting"
domain: "project"
title: "csolution: CubeMX fails to open from VS Code on Linux/macOS with CMSIS Solution extension 1.72"
summary: "The extension started the CubeMX generator launch inside a pseudo terminal on Linux and macOS."
status: "draft"
tool: "csolution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550"
resolution: "workaround"
versions: "Regression in CMSIS Solution extension v1.72; v1.70 works. Validated fix in nightly 1.72.1-3-20261005."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The extension started the CubeMX generator launch inside a pseudo terminal on Linux and macOS. The cbridge detach terminated that pseudo terminal before the generator had finished loading, so CubeMX did not come up. The regression was introduced by #450.

## Fix

Until a fix is released, copy the csolution run command printed in the CMSIS Solution Output channel and run it in a regular VS Code terminal; the reporter confirmed this works. A fix was validated on macOS in nightly build 1.72.1-3-20261005, which the thread does not show as part of a released version.

## Source

Resolution: workaround

Versions: Regression in CMSIS Solution extension v1.72; v1.70 works. Validated fix in nightly 1.72.1-3-20261005.

From [Open-CMSIS-Pack/vscode-cmsis-solution #550](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
