---
id: "tbx-pack-creation-pack-creation-tools"
type: "concept"
domain: "pack"
title: "Pack Creation: Pack Creation Tools"
summary: "The following tools are part of the CMSIS-Toolbox. These tools can be used to develop packs on a local computer and to automate the creation of packs."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#pack-creation-tools"
license: "Apache-2.0"
mode: "V"
---

The following tools are part of the CMSIS-Toolbox. These tools can be used to develop packs on a local computer and to automate the creation of packs.

| Tool           | Description  |
|:---------------|:-------------|
| [**packchk**](https://github.com/Open-CMSIS-Pack/devtools/blob/main/tools/packchk/README.md) | **Pack Validation:** validates the PDSC file against the pack schema and checks referenced files, required metadata, and dependencies. |
| [**svdconv**](https://github.com/Open-CMSIS-Pack/devtools/blob/main/tools/svdconv/SVDConv/README.md) | **SVD Check / Convert:** validate and/or convert System View Description (SVD) files. |
| [**vidx2pidx**](https://github.com/Open-CMSIS-Pack/vidx2pidx/blob/main/README.md) | **Package Index Generator:** check Package index file (PIDX) for indexing in public pack services. |

### Usage

The following section is based on the repositories [DFP-Pack-HandsOn](https://github.com/Open-CMSIS-Pack/DFP-Pack-HandsOn) and [BSP-Pack-HandsOn](https://github.com/Open-CMSIS-Pack/BSP-Pack-HandsOn).  Checkout these packs for local development of pack content.

!!! Tip
    Install the VS Code extension [CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) and related tools. The [Keil Studio Pack](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack) is a collection of such related extensions.

**Step 1:** Create an empty workspace and ensure that development tools are available. When using the [Arm Tools Environment Manager](https://marketplace.visualstudio.com/items?itemName=Arm.environment-manager) this can be configured using the following vand related tools are installed.

```json
{
    "registries": [
        {
            "name": "arm",
            "kind": "artifact",
            "location": "https://artifacts.tools.arm.com/vcpkg-registry"
        }
    ],
    "requires": {
        "arm:compilers/arm/armclang": "6.23.0",
        "arm:compilers/arm/arm-none-eabi-gcc": "14.2.1",
        "arm:compilers/arm/llvm-embedded": "19.1.5",
        "arm:tools/kitware/cmake": "3.31.5",
        "arm:tools/ninja-build/ninja": "1.12.0",
        "arm:tools/open-cmsis-pack/cmsis-toolbox": "2.7.0"
    }
}
```

!!! Tip
    Verify the setup with the commands `cbuild list environment` and `cbuild list toolchains`.

**Step 2:** Register packs for development using these commands:

```txt
cpackget add <workdir>/DFP-Pack-Handson/ACME.ACMECM4_DFP.pdsc
cpackget add <workdir>/BSP-Pack-Handson/ACME.ACME_BSP.pdsc
```

!!! Tip
    The CMSIS-Toolbox now uses this local repositories. Verify the installation with with the commands `cpackget list`, `csolution list devices`, and `csolution list boards`.

!!! Note
    CMSIS-Toolbox 2.7.0 adds an empty `<timestamp></timestamp>` line to the file `$CMSIS_PACK_ROOT/local/local_repository.pidx` which prevents the VS Code extension from using the local pack content. As workaround remove this line.

Content of `$CMSIS_PACK_ROOT/local/local_repository.pidx`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<index schemaVersion="1.1.0">
 <vendor>local repository</vendor>
 <url>file://localhost/C:/Users/reikei01/AppData/Local/Arm/Packs</url>
 <pindex>
  <pdsc vendor="ACME" url="file://localhost/c:/w/DFP-Pack-Handson/" name="ACMECM4_DFP" version="1.1.1"></pdsc>
  <pdsc vendor="ACME" url="file://localhost/C:/w/BSP-Pack-HandsOn/" name="ACME_BSP" version="1.0.0"></pdsc>
 </pindex>
</index>
```

**Step 3:** The various tools have now access to the local packs and you may change the PDSC files. Rename the packs to reflect your products and develop the content starting with the MUST HAVE items listed above.

!!! Tip
    Use the VS Code extension [Red Hat XML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml) for syntax help on the XML format.

**Step 4:** Verify the packs using the following commands:

```txt
packchk <workdir>/DFP-Pack-Handson/ACME.ACMECM4_DFP.pdsc -i $CMSIS_PACK_ROOT/ARM/CMSIS/6.1.0/ARM.CMSIS.pdsc
packchk <workdir>/BSP-Pack-Handson/ACME.ACME_BSP.pdsc -i <workdir>/DFP-Pack-Handson/ACME.ACMECM4_DFP -i $CMSIS_PACK_ROOT/ARM/CMSIS/6.1.0/ARM.CMSIS.pdsc
```

**Step 5:** Verify the Blinky example with a build test in an IDE and execution test on the board.

**Step 6:** Commit the packs to the repository, verify the GitHub action workflows, download the artifacts. Make an end-to-end test of the packs on a different computer.

**Step 7:** [Publish the packs](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html).
