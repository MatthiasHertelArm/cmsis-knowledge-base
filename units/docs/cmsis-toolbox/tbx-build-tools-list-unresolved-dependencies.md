---
id: "tbx-build-tools-list-unresolved-dependencies"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / List Unresolved Dependencies"
summary: "Device, board, and software components are specified as part of the .csolution.yml and .cproject.yml files. Print a list of unresolved project dependencies. The list can be filtered by words provided with the option --filter:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#list-unresolved-dependencies"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

Device, board, and software components are specified as part of the `*.csolution.yml` and `*.cproject.yml` files. Print a list of unresolved project dependencies. The list can be filtered by words provided with the option `--filter`:

```shell
csolution list dependencies mysolution.csolution.yml [-f "WORDS" | -f WORD [-f WORD]...]
```
