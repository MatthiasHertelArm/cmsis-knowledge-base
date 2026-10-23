---
id: "tbx-csolution-project-structure-west-build-system-integration"
type: "concept"
domain: "project"
title: "CSolution Project Structure: West Build System Integration"
summary: "The West build system is a project management system used primarily in the Zephyr ecosystem. The integration in the CMSIS-Toolbox acts as a \"build orchestration wrapper\" around CMake."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#west-build-system-integration"
license: "Apache-2.0"
mode: "V"
---

The West build system is a project management system used primarily in the [Zephyr](https://www.zephyrproject.org/) ecosystem. The integration in the CMSIS-Toolbox acts as a "build orchestration wrapper" around CMake.
The CMSIS-Toolbox connects the `west build` command with the information of the CMSIS-Pack system as shown in the diagram below. For the [selected compiler](#compiler-selection) the related [environment variables for the west build system](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-operation.md#west-integration) are set. When combined with the [VS Code CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) extension, features such as project outline in the CMSIS View or "go-to-definition" with `clangd` are available.

(figure: West Build System Integration)

West projects are specified using the [`west:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#west) node under `projects:` in the `*.csolution.yml` file and can be managed with the `target-types` and `build-types` of the *csolution project*. Note that the `sysbuild` feature of `west` is not supported as the CMSIS-Toolbox manages already related projects.

The usual `cbuild` setup, build, clean, and rebuild operations also apply to West projects. During setup, the integration requests a `compile_commands.json` database from West for editor and language-server support. See [West Integration](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-operation.md#west-integration) for the command mapping.

**Example:**

```yml
solution:
  compiler: AC6

  packs:
    - pack: AlifSemiconductor::Ensemble@^2.0.0-0
    - pack: ARM::CMSIS

  target-types:
    - type: DevKit-E7
      board: Alif Semiconductor::DevKit-E7
      device: Alif Semiconductor::AE722F80F55D5LS
      variables:                            # west board selection
        - west-board: alif_e7_dk_rtss

      target-set:
        - set:
          debugger:
            name: J-Link Server
            port: 3333
            protocol: swd
          images:
            - project-context: rtss_he.Debug
            - project-context: rtss_hp.Release

  build-types:
    - type: Debug
      optimize: debug
      west-defs:                           # west defines
        - CONFIG_DEBUG: y
        - CONFIG_DEBUG_THREAD_INFO: y
        - SE_SERVICES: OFF
        - CMAKE_BUILD_TYPE: Debug

    - type: Release
      optimize: size
      west-defs:                           # west defines
        - SE_SERVICES: OFF
        - CMAKE_BUILD_TYPE: Release

  projects:
    - west:
        app-path: ./alif/samples/drivers/ipm/ipm_arm_mhuv2/rtss_he
        board: $west-board$_he
        device: :M55_HE
    - west:
        app-path: ./alif/samples/drivers/ipm/ipm_arm_mhuv2/rtss_hp
        board: $west-board$_hp
        device: :M55_HP
```

For a multi-board Zephyr example that includes debugging and CI workflows, refer to [Arm-Examples/CMSIS-Zephyr](https://github.com/Arm-Examples/CMSIS-Zephyr).
