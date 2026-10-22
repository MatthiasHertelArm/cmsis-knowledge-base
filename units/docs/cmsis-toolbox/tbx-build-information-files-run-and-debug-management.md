---
id: "tbx-build-information-files-run-and-debug-management"
type: "concept"
domain: "project"
title: "Build Information Files: Run and Debug Management"
summary: "The CMSIS-Toolbox build system manages software packs that contain information about device, board, and software components. It controls the build output (typically ELF/DWARF files), and has provisions for HEX, BIN and post-processing."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#run-and-debug-management"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Toolbox build system manages software packs that contain information about device, board, and software components. It controls the build output (typically ELF/DWARF files), and has provisions for HEX, BIN and post-processing. The [`target-set:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-overview.md#run-and-debug-configuration) node configures the application images and the debugger for a [target-type](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/build-overview.md#configure-related-projects).

The software packs contain information that is the basis for debug and run settings:

- [Flash algorithms](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/flashAlgorithm.html) for programming device memory (defined in DFP) and board memory (defined in BSP).
- [Flash information](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_flashinfo) for device memory (defined in DFP) that uses debugger JTAG/SWD sequences for programming an image.
- On-board debug adapter (a default programming/debug channel) including features.
- Available memory of device and board.
- Device parameters such as processor core(s) and clock speed.
- [Debug Access Sequences](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html) and [System Description Files](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html) that support more complex Cortex-A/R/M configurations.
- Debug Configuration files (`*.dbgconf`) that configure device properties such as trace pins.
- [CMSIS-SVD System View Description (SVD)](https://open-cmsis-pack.github.io/svd-spec/main/index.html) files for viewing device peripherals.
- [CMSIS-View Software Component Viewer Description (SCVD)](https://arm-software.github.io/CMSIS-View/latest/SCVD_Format.html) files for analysis of software components (RTOS, Middleware).

The user may add the following information in the `*.csolution.yml` file:

- [Additional memory](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#add-memory) with flash algorithms for external memory in custom hardware using the [`memory:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#memory) node.
- [Additional images](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#images) that should be programmed or loaded using the [`images:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#images) node.
- [Debugger configuration](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#debugger-configuration) provided by packs can be adjusted using the [`debugger:`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/YML-Input-Format.md#debugger) node.

!!! Note
    The information may be defined at various places. The `*.csolution.yml` file overrules the information from the BSP. The BSP overrules the information from the DFP.

The file `*.cbuild-run.yml` contains for a single `target-type` of a *csolution project* the relevant information for run and debug. The information is collected by the CMSIS-Toolbox and the file name has the format `<solution-name>+<target-type>.cbuild-run.yml` file. It is used by programmers and debuggers in command line or IDE workflows. The information is portable, i.e. from a cloud-hosted CI system to a desktop test system.

(figure: Run and Debug Information Management)

The `<solution-name>+<target-type>.cbuild-run.yml` file represents a single `target-type` of a *csolution project*.

**Example:**

```yml
cbuild-run:
  generated-by: csolution version 2.7.0
  solution: CubeMX.csolution.yml
  target-type: MyBoard_ROM
  compiler: AC6
  device: STMicroelectronics::STM32U585AIIx
  device-pack: Keil::STM32U5xx_DFP@3.0.0
  board: STMicroelectronics::B-U585I-IOT02A:Rev.C
  board-pack: Keil::B-U585I-IOT02A_BSP@2.0.0
  programming:
    - algorithm: ${CMSIS_PACK_ROOT}/Keil/STM32U5xx_DFP/3.0.0/CMSIS/Flash/STM32U5xx_2M_0800.FLM
      start: 0x08000000
      size: 0x00200000
      ram-start: 0x20000000
      ram-size: 0x00008000
    - algorithm: ${CMSIS_PACK_ROOT}/Keil/STM32U5xx_DFP/3.0.0/CMSIS/Flash/STM32U5xx_2M_0C00.FLM
      :
  system-descriptions:
    - file: ${CMSIS_PACK_ROOT}/Keil/STM32U5xx_DFP/3.0.0/CMSIS/SVD/STM32U585.svd
      type: svd
  output:
    - file: out/CubeMX/MyBoard_ROM/Debug/CubeMX.axf
      project: CubeMX
      type: elf

  system-resources:
    memory:
      :

  debugger:
    - name: pyOCD@CMSIS-DAP
      :

  debug-vars:
      :

  debug-sequences:
      :

  debug-topology:
      :
```
