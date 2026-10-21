---
id: "x-create-csolution-github-action-1"
type: "concept"
domain: "devops"
title: "FVP-capable target in csolution debugger settings"
status: "draft"
extracted_from: "proc-create-csolution-github-action"
source: "devops/create-csolution-github-action/SKILL.md"
license: "Apache-2.0"
---

Read `debugger:` directly from each target's selected `target-set` in the `*.csolution.yml`.

A target is FVP-capable when `debugger.model` starts with `FVP`. Use that value as the FVP command and use `debugger.config-file` as its configuration.
