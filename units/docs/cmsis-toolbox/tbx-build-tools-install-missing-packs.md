---
id: "tbx-build-tools-install-missing-packs"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Install Missing Packs"
summary: "Print a list of missing packs required by the example.csolution.yml but not available in the pack repository to the file packs.txt. These missing packs can then be installed using the cpackget tool."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#install-missing-packs"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

Print a list of missing packs required by the `example.csolution.yml` but not available
in the pack repository to the file `packs.txt`. These missing packs can then be installed using the [`cpackget`](#cpackget-invocation) tool.

```shell
csolution list packs example.csolution.yml -m >packs.txt
cpackget update-index               # optional to ensure that pack index is up-to-date
cpackget add -f packs.txt
```
