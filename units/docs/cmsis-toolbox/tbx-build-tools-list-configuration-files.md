---
id: "tbx-build-tools-list-configuration-files"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / List configuration files"
summary: "List all configuration files that belong to software components and are stored in the RTE directory. When updating software packs, it also shows the update status of each file."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#list-configuration-files"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

List all configuration files that belong to software components and are stored in the [RTE directory](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#rte-directory-structure). When [updating software packs](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/CreateApplications.md#update-software-packs), it also shows the update status of each file.

```shell
csolution list configs SimpleTZ.csolution.yml -S
```
