---
id: "tbx-pack-creation-project-examples"
type: "concept"
domain: "pack"
title: "Pack Creation: Project Examples"
summary: "CMSIS-Pack supports Template Projects, Examples, and Reference Applications. Refer to Project Example Types for details. This section explains how these project types are structured and registered within a software pack."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pack-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/#project-examples"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Pack supports *Template Projects*, *Examples*, and *Reference Applications*. Refer to [Project Example Types](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/ReferenceApplications.md#introduction) for details. This section explains how these project types are structured and registered within a software pack.

In addition, packs may contain:

- [*Layers*](#layers) are  pre-configured software components or source code that can be shared across multiple projects.
- [*Code Templates*](#code-templates) are stub source files for middleware components that can be incorporated into user code.

### Support Multiple Compilers

To make project examples independent of a specific compiler toolchain, the `*.csolution.yml` file should include the `select-compiler:` node with a list of tested compilers. When a user or IDE starts such an example, the `compiler:` node that selects the compiler gets added.

**Example:**

```yml
solution:
  description: <brief description of the project example>
  created-for: CMSIS-Toolbox@2.6.0
  cdefault:

  select-compiler:  # list of tested compilers that can be selected
    - compiler: AC6
    - compiler: GCC
    - compiler: IAR
    - compiler: CLANG
      :
```

### Related Examples

The `*.csolution.yml` file may contain several related projects that share the same [`target-types:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#target-types) and [`build-types:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#build-types).

**Example:**

```yml
solution:
      :
  projects:
    - project: BSD_Server/BSD_Server.cproject.yml
    - project: FTP_Server/FTP_Server.cproject.yml
    - project: HTTP_Server/HTTP_Server.cproject.yml
```

### Template Projects

The VSCode extension [CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) supports *template projects* that are part of a DFP or BSP. It is a starting point for a user application and
can be directly compiled, but the functionality is mostly empty. *Template projects* may provide:

- Setup for single-core, TrustZone, or multi-core projects, optional with execution from ROM or RAM.
- Can be device and board specific, optional Configuration Generator.
- May contain other projects that are ready to use (Bootloader, Trusted Firmware).

A *template project* may omit [`device:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#device), [`board:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#board), and [`pack:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#pack) specification in the `*.csolution.yml` file. When a IDE starts a template this information is added depending on user selection.

!!! Note
    *Templates* should compile when the IDE adds above information to the `*.csolution.yml` file. The exception is when *templates* require parts of the code provided by a generator.

**Simple Template:**

A simple *template* only defines one project.

```yml
# A solution is a collection of related projects that share same base configuration.
solution:
  created-for: CMSIS-Toolbox@2.6.0
  cdefault:

  # List of tested compilers that can be selected
  select-compiler:
    - compiler: AC6
    - compiler: GCC
    - compiler: IAR

  target-types:      # empty, filled in by IDE

  # List of different build configurations.
  build-types:
    - type: Debug
      debug: on
      optimize: debug

    - type: Release
      debug: off
      optimize: balanced

  # List related projects.
  projects:
    - project: Simple.cproject.yml
```

**Multi-Target Template:**

A multi-target *template* may contain different configurations for the same target, such as one that executes from ROM and another that executes from RAM. The example below shows how this could be achieved using [`variables:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#variables).

```yml
solution:
      :
  target-types:
    - type: ${Name}_ROM
      variables:
        - RegionsHeader: <path>/memory_flash.h

    - type: ${Name}_RAM
      variables:
        - RegionsHeader: <path>/memory_ram.h
      :
```

In the example above, projects can use the [`linker:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#linker) node in the `*.cproject.yml` file to reference the regions header file of the selected target.

```yml
project:

  linker:
    - regions:  $RegionsHeader$
```

**Board-specific Template:**

Board specific *template projects* provide a meaningful configuration for peripherals on a board. As it is fixed to a board, it may define the *target-type* along with that packs required.

```yml
solution:
      :
  packs:
    - pack: NXP::FRDM-MCXN947_BSP    # do not use pack version as it is part of a BSP
    - pack: NXP::MCXN947_DFP
    - pack: ARM::CMSIS

  target-types:
    - type: MCXN947
      device: NXP::MCXN947VDF
      board: NXP::FRDM-MCXN947
```

**Register Template in PDSC File:**

*Templates* are published using the [`<csolution>` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_csolution_pg.html) in the PDSC file. Device-specific *Templates* should be part of the DFP. Board-specific *templates* should be part of the BSP.

```xml
  <csolution>
    <template name="Simple Device project" path="/device/Simple" file="Simple.csolution.yml" condition="Device_Spec">
      <description>Single-core project with empty main function configured for device</description>
    </template>
    <template name="Simple Board project" path="/board/Simple" file="Simple.csolution.yml" condition="Board_Spec">
      <description>Single-core project with empty main function configured for board</description>
    </template>
  </csolution>
```

### Examples

*Examples* are complete projects that typically run on a board. They should, therefore, specify a `target-type` with [`board:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#board) and list the [`packs:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#packs) that are used, specifically the DFP and BSP.

To minimize maintenance of *Examples* that are part of a pack, consider these rules:

- **IMPORTANT:** Store all files that are part of the [`./RTE` directory](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#rte-directory-structure). These files store configuration and are important for [PLM](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#plm-of-configuration-files).
- Use [`select-compiler:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#select-compiler) when the *Example* works with several toolchains.  Do not specify `compiler:`.
- Specify [minimum pack version](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#pack-name-conventions). Do not store `*.cbuild-pack.yml`.
- The tool selects first `target-type` and first `build-type` when `cbuild-set.yml` is missing. For simple projects, do not store `*.cbuild-set.yml`.
- For simple projects, rely on the `cdefault.yml` file that is provided with CMSIS-Toolbox.

*Examples* that work with several compiler toolchains should use [`select-compiler:`](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#select-compiler) and not define `compiler:` explicitly. The available toolchain's `compiler:` node is added when the *Example* is loaded into the IDE.

When [minimum pack versions](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/YML-Input-Format.md#pack-name-conventions) are specified, the semantic versioning of packs should ensure that newer pack versions work also. As the `*.cbuild-pack.yml` file fixes pack versions, this file should not be stored in the pack.

*Examples* may contain multiple related projects in the `*.csolution.yml` file that, for example, cover different aspects of peripheral or middleware. For such *Examples*, it is not required to store the `*.cbuild-set.yml` file as the tools select the first `target-type` and `build-type` of the `*.csolution.yml` file.

*Examples* that do not require special compiler controls may rely on the [`cdefault.yml` file](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#cdefaultyml) that is provided with CMSIS-Toolbox as this file contains reasonable default settings. For more complex *Examples*, provide a local copy of the `cdefault.yml` file in the same directory as the `*.csolution.yml` file.

Refer to [Toolchain Agnostic Project](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/build-overview.md#toolchain-agnostic-project) for further information.

**`csolution.yml` file of an *Example*:**

```yml
solution:
# Optional: Add a brief description line (recommendation less than 128 characters)
  description: Example that shows the usage of Fault component on a Cortex-M33 with TrustZone

  created-for: CMSIS-Toolbox@2.6.0          # minimum CMSIS-Toolbox version, newer versions will work also
  cdefault:

  select-compiler:
    - compiler: GCC               # GCC is supported
    - compiler: AC6               # AC6 is supported
    - compiler: IAR               # IAR is supported

  packs:
    - pack: Keil::STM32U5xx_DFP@^2.1.0      # minimum compatible pack version
    - pack: Keil::B-U585I-IOT02A_BSP@^1.0.0

  target-types:
    - type: B-U585I-IOT02A
      board: STMicroelectronics::B-U585I-IOT02A
      device: STMicroelectronics::STM32U585AIIx

  build-types:
    - type: Debug
      debug: on
      optimize: debug

    - type: Release
      debug: off
      optimize: balanced

  projects:
    - project: ./Secure/Fault_S.cproject.yml
    - project: ./NonSecure/Fault_NS.cproject.yml
```

**Register *Examples* in PDSC File:**

*Examples* can be part of any pack and are published using the [`<examples>` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html) in the PDSC file. Note that it is possible to register multiple project formats to support different tool environments.

```xml
  <examples>
    <example name="Fault example" folder="Examples/Fault/B-U585I-IOT02A" doc="README.md">
      <description>Example that shows the usage of Fault component on a Cortex-M33 with TrustZone</description>
      <board name="B-U585I-IOT02A" vendor="STMicroelectronics"/>
      <project>
        <environment name="csolution" load="Fault.csolution.yml"/>
        <environment name="uv" load="Fault.uvmpw"/>
      </project>
    </example>
  </examples>
```

### Reference Applications

[*Reference applications*](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/ReferenceApplications.md) can run on many different target hardware boards. Similar to [*template projects*](#template-projects), the `device:` and `board:` along with the required DFP and BSP `pack:` is not specified in the `*.csolution.yml` file.

```yml
solution:
  description: IPv4/IPv6 Network examples
  created-for: CMSIS-Toolbox@2.6.0
  cdefault:

  select-compiler:  # list of tested compilers that can be selected
    - compiler: AC6
    - compiler: GCC
    - compiler: IAR
    - compiler: CLANG

  target-types:
    - type: Name
#     board:           # added during creation of solution
#     variables:
#       - Board-Layer: <board_layer>.clayer.yml
```

!!! Note
    The [MDK-Middleware](https://github.com/ARM-software/MDK-Middleware/tree/main/Examples) contains several *reference applications* that exemplify the overall structure.

**Register *Reference Applications* in PDSC File:**

*Reference Applications* are typically part of a middleware software pack and publish using the [`<examples>` element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html) in the PDSC file. The difference to [*examples*](#examples) is that no `<board> element` is used as the *reference application* is hardware agnostic.

```xml
  <examples>
    </example>
    <example name="Network" doc="README.md" folder="Examples/Network">
      <description>MDK-Middleware: IPv4/IPv6 Client and Server applications via Ethernet</description>
      <project>
        <environment name="csolution" load="Network.csolution.yml"/>
      </project>
    </example>
```
