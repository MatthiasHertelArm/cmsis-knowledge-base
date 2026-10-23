---
id: "tbx-build-tools-specify-cmsis-pack-root-directory"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Specify CMSIS-Pack root directory"
summary: "cpackget is compatible with other CMSIS-Pack management tools, such as the Pack Installer, available in MDK or Eclipse variants. There are two ways to specify the CMSIS-PACK root directory:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#specify-cmsis-pack-root-directory"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

`cpackget` is compatible with other CMSIS-Pack management tools, such as the Pack Installer, available in MDK or Eclipse
variants. There are two ways to specify the CMSIS-PACK root directory:

1. With the `CMSIS_PACK_ROOT` environment variable.
   Refer to [Installation: Environment Variables](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/installation.md#environment-variables).

2. With the option `--pack-root <path>`, for example:

```shell
cpackget add Vendor.PackName --pack-root ./MyLocal/Packs
```

!!! Note
    As the various tools of the CMSIS-Toolbox all rely on the CMSIS-Pack root directory, it is recommended to use the `CMSIS_PACK_ROOT` environment variable.
