---
id: "avh-arm-tools-artifactory-download-with-vcpkg"
type: "concept"
domain: "test"
title: "Arm Tools Artifactory: Download with vcpkg"
summary: "vcpkg is a package management utility that can be used to easily configure and recreate your development environment."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/infrastructure/src/avh_artifactory.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/infrastructure/src/avh_artifactory.md#download-with-vcpkg"
license: "Apache-2.0"
mode: "V"
---

vcpkg is a package management utility that can be used to easily configure and recreate your development environment.

The learning path article
[Install tools on the command line using vcpkg](https://learn.arm.com/learning-paths/microcontrollers/vcpkg-tool-installation/)
provides detailed information on how to install vcpkg on your machine and use it to retrieve specific tool artifacts.

vcpkg is natively integrated into Keil Studio and is configured in many Arm references examples. It is also used in
GitHub CI/CD workflows as explained in avh_gh_actions.

For Arm FVPs, the `vcpkg_configuration.json` file must contain an `"arm:models/arm/avh-fvp"` entry to ensure the
download of the models. For example:

```json
{
  "registries": [
    {
      "kind": "artifact",
      "location": "https://artifacts.tools.arm.com/vcpkg-registry"
      "name": "arm"
    }
  ],
  "requires": {
    "arm:models/arm/avh-fvp": "^11.30.29"
  }
}
```
