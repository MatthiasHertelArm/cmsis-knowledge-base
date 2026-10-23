---
id: "tbx-build-tools-list-project-templates"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / List Project Templates"
summary: "List project templates provided by installed software packs. Each entry identifies the template and its originating pack. Use --filter to restrict the list. The --verbose option adds the template description, directory, and .csolution.yml file."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#list-project-templates"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

List project templates provided by installed software packs. Each entry identifies the template and its originating pack. Use `--filter` to restrict the list. The `--verbose` option adds the template description, directory, and `*.csolution.yml` file.

```shell
csolution list templates
csolution list templates --filter CubeMX --verbose
```

Example output:

```text
CubeMX Basic solution (Keil::STM32U5xx_DFP@3.2.0)
  description: Create a CubeMX basic solution with project
  path: <pack-root>/Keil/STM32U5xx_DFP/3.2.0/Templates/CubeMX
  file: <pack-root>/Keil/STM32U5xx_DFP/3.2.0/Templates/CubeMX/CubeMX.csolution.yml
```
