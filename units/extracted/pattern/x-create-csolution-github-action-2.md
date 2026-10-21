---
id: "x-create-csolution-github-action-2"
type: "pattern"
domain: "devops"
title: "Build one target type of a CMSIS solution with pack installation"
status: "draft"
extracted_from: "proc-create-csolution-github-action"
source: "devops/create-csolution-github-action/SKILL.md"
license: "Apache-2.0"
---

Use `cbuild <solution>.csolution.yml --active <target-type> --packs`. Do not replace `--active` with a context expression.
