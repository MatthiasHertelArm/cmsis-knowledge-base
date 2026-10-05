---
id: "avh-use-with-keil-studio-vcpkg-configuration"
type: "concept"
domain: "test"
title: "Use with Keil Studio: vcpkg configuration"
summary: "Keil Studio relies on the Arm Tools Environment Manager extension to setup the development environment from Arm Tools Artifactory using Microsoft vcpkg."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/avh_mdk_vscode.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/avh_mdk_vscode.md#vcpkg-configuration"
license: "Apache-2.0"
mode: "V"
---

Keil Studio relies on the
[Arm Tools Environment Manager](https://marketplace.visualstudio.com/items?itemName=Arm.environment-manager) extension
to setup the development environment from Arm Tools Artifactory using Microsoft vcpkg. The vcpkg manifest file
`vcpkg_configuration.json` must contain the requirement for Arm FVPs models, in the same way as explained in
avh_fvp_vcpkg. For example:

```json
{
  "registries": [
    {
      "name": "arm"
      "kind": "artifact",
      "location": "https://artifacts.tools.arm.com/vcpkg-registry"
    }
  ],
  "requires": {
    "arm:models/arm/avh-fvp": "^11.30.29"
  }
}
```

> **Note**
> In Keil Studio other tools are usually also present for build and debug tasks such as CMSIS-Toolbox, a compiler
> toolchain, and others.
