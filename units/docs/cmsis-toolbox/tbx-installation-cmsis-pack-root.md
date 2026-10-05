---
id: "tbx-installation-cmsis-pack-root"
type: "concept"
domain: "project"
title: "Installation: CMSIS_PACK_ROOT"
summary: "The environment variable CMSISPACKROOT defines the location of the directory that stores the software packs. This directory has the following structure."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/installation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/installation/#cmsis-pack-root"
license: "Apache-2.0"
mode: "V"
---

The [environment variable `CMSIS_PACK_ROOT`](#environment-variables) defines the location of the directory that stores the software packs. This directory has the following structure.

Content of `CMSIS_PACK_ROOT` | Description
:----------------------------|:----------------
`pack.idx`                   | Empty file that is touched (timestamp is updated) when packs are added or removed.
`/.Web`                      | Contains `*.pdsc` files available on public web pages.
`/.Web/index.pidx`           | An index file that lists publicly available software packs.
`/.Download`                 | A local cache of packs that are downloaded.
`/.Local`                    | Stores the file `local_repository.pidx` that refers local `*.pdsc` files during pack development. Refer to  [install a repository](https://open-cmsis-pack.github.io/cmsis-toolbox/installation/build-tools.md#install-a-repository) for more information.
`/<vendor>/<name>/<version>` | Extracted software packs that are available for development using the CMSIS-Toolbox.

!!! Note
    For more details, refer to the [CMSIS_PACK_ROOT Directory Wiki page](https://github.com/Open-CMSIS-Pack/devtools/wiki/The-CMSIS-PACK-Root-Directory).
