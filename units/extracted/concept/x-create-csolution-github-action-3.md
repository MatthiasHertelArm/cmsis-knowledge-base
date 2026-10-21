---
id: "x-create-csolution-github-action-3"
type: "concept"
domain: "devops"
title: "Loaded solution and active target in .vscode/cmsis.json"
status: "draft"
extracted_from: "proc-create-csolution-github-action"
source: "devops/create-csolution-github-action/SKILL.md"
license: "Apache-2.0"
---

Find the Git repository root and parse `.vscode/cmsis.json` as JSON.
Read `targetSet`. Its key identifies the loaded solution and `activeTargetType` identifies the active target.
