---
id: "tbx-build-tools-list-all-software-packs"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / List all software packs"
summary: "List of all installed packs that are available in the CMSIS-Pack root directory."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#list-all-software-packs"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

List of all installed packs that are available in the CMSIS-Pack root directory.

```shell
cpackget list
```

This will include all packs that are installed via `cpackget add` command, regardless of the source of the software
pack. There are also a couple of flags that allow listing extra information.

List all cached packs that are present in the `.Download/` folder:

```shell
cpackget list --cached
```

List all non-deprecated packs present in the local copy of the **Pack Index File** (`index.pidx`):

```shell
cpackget list --public
```

List only deprecated packs in the public index:

```shell
cpackget list --deprecated
```

Deprecated packs and their PDSC files are excluded from normal public listings and bulk PDSC downloads, but a deprecated pack can still be installed by specifying its pack ID explicitly.

!!! Note
    [Update Pack Index File](#update-pack-index) before using the `list` command to list all public software packs.
