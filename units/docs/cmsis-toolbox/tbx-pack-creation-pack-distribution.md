---
id: "tbx-pack-creation-pack-distribution"
type: "concept"
domain: "pack"
title: "Pack Creation: Pack Distribution"
summary: "The section Publish a CMSIS-Pack in the Open-CMSIS-Pack specification describes the pack distribution process. There are multiple distribution options, ranging from local installation to publishing via web services."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#pack-distribution"
license: "Apache-2.0"
mode: "V"
---

The section [Publish a CMSIS-Pack](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html) in the [Open-CMSIS-Pack specification](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec) describes the pack distribution process. There are multiple distribution options, ranging from [local installation](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html#cp_LocalInstallation) to publishing via [web services](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html#cp_WebDownload).

### Validate a Pack Index

Before publishing a vendor index (`*.vidx`), convert it to a package index (`*.pidx`) and test the result in a separate pack root:

```shell
vidx2pidx <index>.vidx --output index.pidx
cpackget init --pack-root packroot index.pidx
cpackget list --public --pack-root packroot
```

The `list` command shows the packs found in the generated package index. Install each listed pack to verify that it can be downloaded and installed successfully:

```shell
cpackget add Vendor::PackName --pack-root packroot
```

### GitHub Pack Distribution

Several vendors use GitHub for pack distribution today. [Alif Semiconductor](https://www.keil.arm.com/packs/?q=Alif&pack) is a good example:

- [github.com/alifsemi/alif_cmsis_packs](https://github.com/alifsemi/alif_cmsis_packs) contains the `*.pidx` index file that references all public packs (including versions) provided by Alif.
  - This index file is submitted **once by email** to the [pack index service](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html#cp_KeilComPack) for the relevant tools (mailto:cmsis@arm.com for Arm Tools, mailto:cmsis@iar.com for IAR Tools).
  - Update this `*.pidx` file to publish new packs or new versions. Arm scans vendor `*.pidx` index files once per day and updates the web content.
- The packs themselves are located in separate GitHub repositories. The `*.pdsc` file of a pack contains the `url` and `repo` elements that tools use to update the pack or consume it as a [repository during development](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-tools.md#install-a-repository).

Refer to [GitHub-hosted packs](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html#cp_GitHubHosting) in the  [Open-CMSIS-Pack specification](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec) for details on the `*.pidx` and `*.pdsc` file content.
