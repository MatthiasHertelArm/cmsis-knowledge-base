---
id: "tbx-build-tools-initialize-cmsis-pack-root-directory"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Initialize CMSIS-Pack root directory"
summary: "CMSIS-Packs are typically distributed via a public web service that offers a Pack Index File of available software packs. To initialize the CMSIS-Pack root directory, run the command:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#initialize-cmsis-pack-root-directory"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

CMSIS-Packs are typically distributed via a public web service that offers a
[**Pack Index File**](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html#packIndexFile)
of available software packs. To initialize the CMSIS-Pack root directory, run the command:

```shell
cpackget init https://www.keil.com/pack/index.pidx
```

This command creates in the CMSIS-PACK root directory the following sub-directories.

Sub-Directory   | Content
:---------------|:------------------------
`.Web`          | [**Pack Index File**](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html#packIndexFile) of a public web service and cached `*.PDSC` files for packs that have been requested.
`.Download`     | Packs that are installed from a web service. Stores `*.PDSC` pack description file, `*.pack` content file, and related license information.
`.Local`        | Index file `local_repository.pidx` that points to local installations for the development of a software pack. Contains also the `*.PDSC` files from private software packs.

The `cpackget init` command [initializes the CMSIS-Pack root directory](#initialize-cmsis-pack-root-directory) but does not download PDSC files. Combined with the option `--all-pdsc-files` it also downloads the PDSC files available in the public index, except those of deprecated packs. Add `--deprecated` to include deprecated PDSC files.

```shell
cpackget init https://www.keil.com/pack/index.pidx --all-pdsc-files
cpackget init https://www.keil.com/pack/index.pidx --all-pdsc-files --deprecated
```
