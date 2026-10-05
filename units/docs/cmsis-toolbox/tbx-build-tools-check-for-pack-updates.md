---
id: "tbx-build-tools-check-for-pack-updates"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Check for Pack Updates"
summary: "Print the available updates for packs used by an existing project. With the option --verbose, the output includes release notes for newer versions and the local path of project-specified packs, when available."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#check-for-pack-updates"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

Print the available updates for packs used by an existing project. With the option `--verbose`, the output includes release notes for newer versions and the local path of project-specified packs, when available. The list can be filtered by words provided with the option `--filter`:

```shell
csolution check pack-updates mysolution.csolution.yml --verbose --filter "USB"
```
