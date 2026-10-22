---
id: "tbx-csolution-project-format-arm-fvp"
type: "concept"
domain: "project"
title: "CSolution Project Format: Debugger Configuration / Arm-FVP"
summary: "This section lists options that are specific to the FVP simulation models. FVPs are configurable simulation models that are designed for software validation. An FVP represents one or more Arm processors."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#arm-fvp"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger Configuration_

This section lists options that are specific to the [FVP](https://arm-software.github.io/AVH/main/simulation/html/index.html) simulation models. FVPs are configurable simulation models that are designed for software validation. An FVP represents one or more Arm processors.

#### `debugger:` for Arm-FVP

debugger:                         |              | Description
:---------------------------------|:-------------|:-----------------------------------------------
    `name:`        | **Required** | Identifies the debug adapter with `Arm-FVP`.
    `model:`       |   Optional   | Filename (optionally with path) of the FVP executable. Default: `FVP_MPS2_Cortex-M3`.
    `config-file:` |   Optional   | Path and filename of the [FVP configuration file](https://arm-software.github.io/AVH/main/simulation/html/using.html).
    `args:`        |   Optional   | Miscellaneous [command line arguments](https://arm-software.github.io/AVH/main/simulation/html/using.html).

The following `model:` executables are installed from the [Arm Tools Artifactory](https://www.keil.arm.com/artifacts/#models/arm/avh-fvp). You should use these models in combination with a `pack:` and `device:` as listed under 
["CMSIS-based projects for FVPs"](https://arm-software.github.io/AVH/main/simulation/html/avh_fvp_cmsis.html). The PATH environment variable of your system can define the path to the FVP executable (then only the `model:` name from the list below is required). Optionally an explicit path can be specified in the `model:` node.

`model:`                         | Simulation Model Represents
:--------------------------------|:---------------------------------
`FVP_Corstone 300`               | [Arm Corstone 300](https://developer.arm.com/documentation/100966/1128/Arm--Corstone-SSE-300-FVP) Reference Platform with Cortex-M55
`FVP_Corstone_SSE-300_Ethos-U55` | [Arm Corstone 300](https://developer.arm.com/documentation/100966/1128/Arm--Corstone-SSE-300-FVP) Reference Platform with Cortex-M55 and Ethos-U55
`FVP_Corstone_SSE-300_Ethos-U65` | [Arm Corstone 300](https://developer.arm.com/documentation/100966/1128/Arm--Corstone-SSE-300-FVP) Reference Platform with Cortex-M55 and Ethos-U65
`FVP_Corstone 310`               | [Arm Corstone 310](https://developer.arm.com/documentation/102778) Reference Platform with Cortex-M85 and Ethos-U55.
`FVP_Corstone_SSE-310_Ethos-U65` | [Arm Corstone 310](https://developer.arm.com/documentation/102778) Reference Platform with Cortex-M85 and Ethos-U65.
`FVP_Corstone 315`               | [Arm Corstone 315](https://developer.arm.com/documentation/109395) Reference Platform with Cortex-M85, Ethos-U65, and Mali-C55.
`FVP_Corstone 320`               | [Arm Corstone 320](https://developer.arm.com/documentation/109760) Reference Platform with Cortex-M85, Ethos-U85, and Mali-C55.
`FVP_MPS2_Cortex-M0`             | [Arm Microcontroller Prototyping System with Cortex-M0](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M0)
`FVP_MPS2_Cortex-M0plus`         | [Arm Microcontroller Prototyping System with Cortex-M0+](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M0plus)
`FVP_MPS2_Cortex-M3`             | [Arm Microcontroller Prototyping System with Cortex-M3](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M3)
`FVP_MPS2_Cortex-M4`             | [Arm Microcontroller Prototyping System with Cortex-M4](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M4)
`FVP_MPS2_Cortex-M7`             | [Arm Microcontroller Prototyping System with Cortex-M7](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M7)
`FVP_MPS2_Cortex-M23`            | [Arm Microcontroller Prototyping System with Cortex-M23](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M23)
`FVP_MPS2_Cortex-M33`            | [Arm Microcontroller Prototyping System with Cortex-M33](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M33)
`FVP_MPS2_Cortex-M35P`           | [Arm Microcontroller Prototyping System with Cortex-M35P](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M35P)
`FVP_MPS2_Cortex-M52`            | [Arm Microcontroller Prototyping System with Cortex-M52](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M52)
`FVP_MPS2_Cortex-M55`            | [Arm Microcontroller Prototyping System with Cortex-M55](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M55)
`FVP_MPS2_Cortex-M85`            | [Arm Microcontroller Prototyping System with Cortex-M85](https://developer.arm.com/documentation/100966/latest/MPS2-Platform-FVPs/FVP-MPS2-Cortex-M85)

**Example:**

```yml
debugger:
  name: CMSIS-DAP@Arm-Debugger
  model:  FVP_Corstone_SSE-320
  config-file: ./FVP_Config.txt
  args: --simlimit 600            # stop simulation after 600 seconds
```
