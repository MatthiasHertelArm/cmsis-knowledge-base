---
id: "tbx-csolution-project-format-project-file-structure"
type: "concept"
domain: "project"
title: "CSolution Project Format: Project File Structure"
summary: "The table below explains the top-level elements in each of the different .yml input files that define the overall application."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#project-file-structure"
license: "Apache-2.0"
mode: "V"
---

The table below explains the top-level elements in each of the different `*.yml` input files that define the overall application.

Keyword                          | Description
:--------------------------------|:------------------------------------
[`default:`](#cdefault)          | Start of `cdefault.yml` file that is used to setup the compiler along with some compiler-specific controls.
[`solution:`](#solution)         | Start of `*.csolution.yml` file that [collects related projects](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#project-examples) along with `build-types:` and `target-types:`.
[`project:`](#project)           | Start of `*.cproject.yml` file that defines files, components, and layers which can be independently translated to a binary image or library.
[`layer:`](#layer)               | Start of `*.clayer.yml` file that contains pre-configured software components along with source files.
