---
id: "tbx-configure-stm32-devices-with-cubem-simple-project"
type: "concept"
domain: "project"
title: "Configure STM32 Devices with CubeMX: Simple Project"
summary: "Below is a simple project that just adds the CubeMX-generated components."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/CubeMX.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/#simple-project"
license: "Apache-2.0"
mode: "V"
---

Below is a simple project that just adds the CubeMX-generated components.

!!! Tip
    The packs required for boards and devices are listed on [www.keil.arm.com/boards](https://www.keil.arm.com/boards/) and [www.keil.arm.com/devices](https://www.keil.arm.com/devices/).

**File: `CubeMX.csolution.yml`**

```yml
solution:
  created-for: CMSIS-Toolbox@2.14.0
  description: Simple CubeMX example
  cdefault:                                   # use toolchain default settings
  compiler: AC6                               # select toolchain

# it is recommended to list the pack or packs that define the device or board used in the csolution.yml file
  packs:
    - pack: ARM::CMSIS                        # CMSIS pack is required for most projects
    - pack: Keil::B-U585I-IOT02A_BSP
    - pack: Keil::STM32U5xx_DFP@^3.0.0

  target-types:
    - type: MyBoard                           # My evaluation kit
      board: B-U585I-IOT02A                   # Board name as defined by the pack
      target-set:
        - set: Debug
          images:
            - project-context: CubeMX.Debug
        - set: Release
          images:
            - project-context: CubeMX.Release

  build-types:
    - type: Debug                             # toolchain options for 'debug'
      debug: on
      optimize: none

    - type: Release                           # toolchain options for 'release'
      debug: off
      optimize: balanced

  projects:                                   # list related projects
    - project: ./CubeMX.cproject.yml
```

**File: `CubeMX.cproject.yml`**

```yml
project:
  components:
    - component: CMSIS:CORE                   # CMSIS-Core component is required
    - component: Device:CubeMX                # Component that connects to CubeMX
```

Such a project cannot be directly built, as initially, the `*.cgen.yml` file is missing. It requires to run the CubeMX generator.  Before you start, you may need to [`install missing packs`](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/build-tools.md#install-missing-packs).

- Identify the required generator and the directory where the generated files are stored with:

```bash
csolution CubeMX.csolution.yml list generators --active MyBoard@Debug --verbose
CubeMX (Global Registered Generator)    # generator name
  base-dir: STM32CubeMX/MyBoard         # directory for generated files
    context: CubeMX.Debug+MyBoard       # context that uses this directory
```

- Use the information above to run the generator:

```bash
csolution CubeMX.csolution.yml run --generator CubeMX --active MyBoard@Debug
```

   This starts CubeMX and passes the information about the selected board, device, and selected toolchain. For a project that selects a board, CubeMX imports the default configuration for it. In CubeMX, review and adjust configuration options as required for your application, then click the button `GENERATE CODE`. The generated files will be stored in the directory `STM32CubeMX/MyBoard`.

- Build the project using this command:

```bash
cbuild CubeMX.csolution.yml --active MyBoard@Debug --update-rte
```

!!! Note
    You may run the CubeMX generator at any time to change the configuration setting of your device or board.

**Directory with generated files**

CubeMX generates the following content in the generator output directory of the *csolution project*. In our example, the generator output directory is `STM32CubeMX/MyBoard`.

Directory `STM32CubeMX/MyBoard`     | Content
:-----------------------------------|:---------------
`CubeMX.cgen.yml`                   | Generator import file that adds the CubeMX generated files to  the *csolution project*.
`MX_Device/MX_Device.h`             | Header file with configuration settings for CMSIS software components.
`STM32CubeMX/STM32CubeMX.ioc`       | CubeMX native project file that includes settings.
`STM32CubeMX/.mxproject`            | CubeMX project metadata used by `cbridge` to import generated sources, include paths, and third-party software.
`STM32CubeMX/Src`                   | CubeMX generated application code: `main.c` and STM32 setup code.
`STM32CubeMX/Inc`                   | Header files for CubeMX generated application code.
`STM32CubeMX/EWARM`                 | Project files for IAR; only startup code and linker scripts are used for *csolution projects*.
`STM32CubeMX/STM32CubeIDE`          | Project files for STM32CubeIDE (GCC); only startup code and linker scripts are used for *csolution projects*.
`STM32CubeMX/MDK-ARM`               | Project files for MDK version 5; only startup code and linker scripts are used for *csolution projects*.

!!! Note
    CubeMX generates only the directory for the selected toolchain, which is either `STM32CubeMX/EWARM`, `STM32CubeMX/STM32CubeIDE`, or `STM32CubeMX/MDK-ARM`.

**Content of Generator Import File: `CubeMX.cgen.yml`**

The file `*.cgen.yml` lists the files and settings that are generated by CubeMX and imported in the *csolution project*. The files under `group: CubeMX` may be modified by the user in sections marked with `USER CODE BEGIN` and `USER CODE END` to implement the application-specific features. In the file `*.cproject.yml` additional [user files](https://open-cmsis-pack.github.io/cmsis-toolbox/CubeMX/YML-Input-Format.md#files) can be added.

The `cbridge` utility also reads each third-party software component selected in CubeMX from the `.mxproject` file. It adds the component's include paths, C source files, and assembly source files to `*.cgen.yml`. Each component is represented by a separate group named after the third-party component; a vendor and version in the CubeMX name are omitted from the group name. These generated entries are updated when CubeMX is run again and do not need to be duplicated manually in `*.cproject.yml`.

```yml
generator-import:
  for-device: STM32U585AIIx
  for-board: B-U585I-IOT02A
  define:
    - USE_FULL_LL_DRIVER
    - USE_HAL_DRIVER
    - STM32U585xx
  add-path:
    - ./STM32CubeMX/Drivers/STM32U5xx_HAL_Driver/Inc
    - ./STM32CubeMX/Drivers/STM32U5xx_HAL_Driver/Inc/Legacy
    - ./STM32CubeMX/Drivers/CMSIS/Device/ST/STM32U5xx/Include
    - ./STM32CubeMX/Inc
    - ./MX_Device/CubeMX
    - ./STM32CubeMX/Middlewares/ThirdPartyLibrary/include
  groups:
    - group: CubeMX
      files:
        - file: ./STM32CubeMX/Src/main.c
        - file: ./STM32CubeMX/Src/stm32u5xx_it.c
        - file: ./STM32CubeMX/Src/stm32u5xx_hal_msp.c
        - file: ./STM32CubeMX/MDK-ARM/startup_stm32u585xx.s
        - file: ./STM32CubeMX/Src/system_stm32u5xx.c
    - group: STM32 HAL Driver
      files:
        - file: ./STM32CubeMX/Drivers/STM32U5xx_HAL_Driver/Src/stm32u5xx_ll_utils.c
        - file: ./STM32CubeMX/Drivers/STM32U5xx_HAL_Driver/Src/stm32u5xx_ll_exti.c
            :
        - file: ./STM32CubeMX/Drivers/STM32U5xx_HAL_Driver/Src/stm32u5xx_hal_pcd_ex.c
        - file: ./STM32CubeMX/Drivers/STM32U5xx_HAL_Driver/Src/stm32u5xx_ll_usb.c
    - group: ThirdPartyLibrary
      files:
        - file: ./STM32CubeMX/Middlewares/ThirdPartyLibrary/src/library.c
        - file: ./STM32CubeMX/Middlewares/ThirdPartyLibrary/src/library_asm.s
```
