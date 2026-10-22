---
id: "tbx-build-tools-update-pack-index"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Update Pack Index"
summary: "When new software packs are available on a public web service, the local copy of the Pack Index File requires an update. To update the Pack Index File, run:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#update-pack-index"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

When new software packs are available on a public web service, the local copy of the **Pack Index File** requires an update. To update the **Pack Index File**, run:

```shell
cpackget update-index
```

The option `--sparse` avoids updating the PDSC files and improves, therefore, the speed.

```shell
cpackget update-index --sparse
```

Use the option `--all-pdsc-files` to download all current PDSC files available in the public index. PDSC files of deprecated packs are excluded by default; add `--deprecated` to include them.

```shell
cpackget update-index --all-pdsc-files
cpackget update-index --all-pdsc-files --deprecated
```
