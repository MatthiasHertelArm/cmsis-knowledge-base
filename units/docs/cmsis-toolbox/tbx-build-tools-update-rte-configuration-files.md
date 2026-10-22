---
id: "tbx-build-tools-update-rte-configuration-files"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Update RTE Configuration Files"
summary: "The Component Configuration​ is stored in the RTE directory. When files are missing or new software pack versions are installed, it might be required to update the RTE configuration files:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#update-rte-configuration-files"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

The [Component Configuration​](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#directory-structure) is stored in the [RTE directory](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#rte-directory-structure). When files are missing or new software pack versions are installed, it might be required to update the RTE configuration files:

```shell
csolution update-rte example.csolution.yml
```
