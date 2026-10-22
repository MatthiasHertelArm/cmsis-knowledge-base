---
id: "tbx-csolution-project-structure-native-cmake-build-integration"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Native CMake Build Integration"
summary: "Native CMake projects can be integrated into a csolution project without a .cproject.yml file. The CMSIS-Toolbox configures and builds each project using the source directory, generator, configure options, and optional build target specified in the cmake: node."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#native-cmake-build-integration"
license: "Apache-2.0"
mode: "V"
---

Native CMake projects can be integrated into a *csolution project* without a `*.cproject.yml` file. The CMSIS-Toolbox configures and builds each project using the source directory, generator, configure options, and optional build target specified in the [`cmake:` node](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#cmake-build).

CMake projects are listed under `projects:` in the `*.csolution.yml` file and participate in the solution's `target-types:` and `build-types:`. Their declared output images are included in the generated [`*.cbuild-run.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-CBuild-Format.md#run-and-debug-management) file and can therefore be combined with images from other project contexts for programming and debugging.

The standard build commands also apply to native CMake project contexts:

```shell
cbuild setup MySolution.csolution.yml --active DualCoreDevice
cbuild MySolution.csolution.yml --active DualCoreDevice
cbuild MySolution.csolution.yml --active DualCoreDevice --clean
cbuild MySolution.csolution.yml --active DualCoreDevice --rebuild
```

The native project remains responsible for its `CMakeLists.txt`, toolchain setup, build targets, and generated files. CMSIS-Toolbox provides orchestration and records the declared images; it does not translate the native project into a `*.cproject.yml` file. Paths under `images:` identify outputs relative to the native project's context output directory.

**Example:**

```yml
solution:
  target-types:
    - type: DualCoreDevice
      device: Vendor::DualCoreDevice

  projects:
    - cmake:
        source: ./core0
        device: :Core0
        images:
          - image: build/core0.elf
            type: elf
```

For a complete application that integrates a native CMake project with CMSIS-Toolbox, refer to [Arm-Examples/CMSIS-CMake](https://github.com/Arm-Examples/CMSIS-CMake).
