---
id: "tbx-build-tools-remove-packs"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Remove packs"
summary: "The commands below demonstrate how to remove packs. This is independent of how the software pack was added."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#remove-packs"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

The commands below demonstrate how to remove packs. This is independent of how the software pack was added.

Remove a software pack with a specific version:

```shell
cpackget rm Vendor.PackName.x.y.z      # or
cpackget rm Vendor::PackName@x.y.z
```

Remove all versions of a software pack:

```shell
cpackget rm Vendor.PackName            # or
cpackget rm Vendor::PackName
```

The procedure is the same as above, but you should also remove the cached files related to this pack from the `.Download/` directory.

```shell
cpackget rm --purge Vendor.PackName`
```

Remove a pack that was [installed via a repository](#install-a-repository).

```shell
cpackget rm Vendor.PackName.pdsc
```

!!! Note
    Remove a local pack with `cpackget rm` before deleting or moving its PDSC file.
