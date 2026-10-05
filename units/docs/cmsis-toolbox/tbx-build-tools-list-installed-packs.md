---
id: "tbx-build-tools-list-installed-packs"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / List Installed Packs"
summary: "Print a list of installed packs. The list can be filtered by words provided with the option --filter:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#list-installed-packs"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

Print a list of installed packs. The list can be filtered by words provided with the option `--filter`:

```shell
csolution list packs [--filter "string" ]
```

Print a list of packs that are required by the `example.csolution.yml`.

```shell
csolution list packs example.csolution.yml
```
