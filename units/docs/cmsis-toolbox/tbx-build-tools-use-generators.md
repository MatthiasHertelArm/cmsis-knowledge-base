---
id: "tbx-build-tools-use-generators"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Use Generators"
summary: "List external code generators that are used to create software components. It outputs the generator ID that is required for the run command. When using the option --verbose, the generator out directory is listed."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#use-generators"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

List external code generators that are used to create software components. It outputs the generator ID that is required for the `run` command. When using the option `--verbose`, the generator out directory is listed.

```shell
csolution list generators mysolution.csolution.yml -v
```

Run a generator (in this case, STM32CubeMX) for a specific project context.  Note that the context can be omitted when the same generator output directory is used.

```shell
csolution run -g CubeMX mysolution.csolution.yml -c Blinky.Debug+STM32L4
```
