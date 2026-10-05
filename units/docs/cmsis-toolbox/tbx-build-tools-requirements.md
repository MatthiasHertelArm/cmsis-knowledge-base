---
id: "tbx-build-tools-requirements"
type: "concept"
domain: "project"
title: "Build Tools: Requirements"
summary: "Install the CMSIS-Toolbox as described in chapter Installation."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#requirements"
license: "Apache-2.0"
mode: "V"
---

Install the CMSIS-Toolbox as described in chapter [Installation](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/installation.md).

The CMSIS-Pack repository must be present in the host development environment.

There are several ways to configure the CMSIS-Pack repository:

- Use the **`cpackget` Package Installer** command `init` to [initialize the CMSIS-Pack root directory](#initialize-cmsis-pack-root-directory), [update the pack index file](#update-pack-index). Then [add software packs](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-tools.md#add-packs).

- Share an existing CMSIS-Pack repository (i.e. from an IDE) via the environment variable `CMSIS_PACK_ROOT`.
