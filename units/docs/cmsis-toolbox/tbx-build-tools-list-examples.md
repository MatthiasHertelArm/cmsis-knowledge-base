---
id: "tbx-build-tools-list-examples"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / List Examples"
summary: "List examples provided by the installed software packs. Each entry identifies the example and its originating pack. Use one or more --filter options to find matching examples."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#list-examples"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

List examples provided by the installed software packs. Each entry identifies the example and its originating pack. Use one or more `--filter` options to find matching examples. The `--verbose` option adds the description, documentation, supported development environments, source folder, load file, and supported boards when that information is provided by the pack.

```shell
csolution list examples
csolution list examples --filter Blinky
csolution list examples --filter Blinky --filter STM32 --verbose
```

Example output:

```text
Blinky (Keil::B-U585I-IOT02A_BSP@3.0.0)
  description: CMSIS-RTOS2 Blinky example with VIO
  environment: csolution
    load: <pack-root>/Keil/B-U585I-IOT02A_BSP/3.0.0/Examples/Blinky/Blinky.csolution.yml
```
