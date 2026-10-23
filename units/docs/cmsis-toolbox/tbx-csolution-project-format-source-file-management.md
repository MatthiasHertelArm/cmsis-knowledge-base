---
id: "tbx-csolution-project-format-source-file-management"
type: "concept"
domain: "project"
title: "CSolution Project Format: Source File Management"
summary: "Keyword | Used in files | Description :----------------|:---------------------------------|:------------------------------------ groups: | .cproject.yml, .clayer.yml | Start of a list that adds source groups and files to a project or layer."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#source-file-management"
license: "Apache-2.0"
mode: "V"
---

Keyword          | Used in files                    | Description
:----------------|:---------------------------------|:------------------------------------
`groups:`        | `*.cproject.yml`, `*.clayer.yml` | Start of a list that adds [source groups and files](#source-file-management) to a project or layer.
`layers:`        | `*.cproject.yml`                 | Start of a list that adds software layers to a project.
`components:`    | `*.cproject.yml`, `*.clayer.yml` | Start of a list that adds software components to a project or layer.
