---
id: "ocp-mdk-middleware-reference-applicati-demo-prerequisites"
type: "concept"
domain: "project"
title: "MDK-Middleware Reference Applications Demo: Demo Prerequisites"
summary: "MDK-Middleware Reference Applications Demo: Demo Prerequisites"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/Create-Scalable-SW@8b5a61f:Demo/MDK-MW_RefApp.md"
doc_source: "https://github.com/Open-CMSIS-Pack/Create-Scalable-SW/blob/8b5a61f/Demo/MDK-MW_RefApp.md#demo-prerequisites"
license: "Apache-2.0"
mode: "V"
---

- Visual Studio Code with [Arm Keil Studio Pack extensions](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack)
- [Tools avaialble via vcpkg](https://www.keil.arm.com/artifacts/)
  - [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases/)
  - Arm Compiler for Embedded
  - GCC compiler for ARM CPUs
- [CMSIS-Toolbox 2.5.0-devint1](https://github.com/brondani/cmsis-toolbox/releases/tag/2.5.0-devint1) (when using STM32CubeMX)
- [CMSIS Packs - public pack index](https://www.keil.arm.com/packs/)
  - [CMSIS 6.1.0](https://www.keil.arm.com/packs/cmsis-arm/versions/)
  - [CMSIS-Compiler 2.1.0](https://www.keil.arm.com/packs/cmsis-compiler-arm/versions/)
  - [CMSIS-RTX 5.9.0](https://www.keil.arm.com/packs/cmsis-rtx-arm/versions/)
  - Target: NXP EVKB-IMXRT1050 Board (Mounted Device: MIMXRT1052DVL6B)
    - [EVKB-IMXRT1050_BSP 18.0.0](https://www.keil.arm.com/packs/evkb-imxrt1050_bsp-nxp/versions/)
    - [MIMXRT1052_DFP 18.0.0](https://www.keil.arm.com/packs/mimxrt1052_dfp-nxp/devices/)
- CMSIS Packs - public repos [mapped as software pack](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/build-tools.md#install-a-repository)
  - [MDK-Middleware 8.0.0-dev](https://github.com/ARM-software/MDK-Middleware)  
    Install pack: `cpackget add <local_path>/Keil.MDK-Middleware.pdsc`
  - Target: STMicroelectronics B-U585I-IOT02A Board (Mounted Device: STM32U585AIIx)
    - [B-U585I-IOT02A_BSP 2.0.0-dev](https://github.com/Open-CMSIS-Pack/ST_B-U585I-IOT02A_BSP)  
      Install pack: `cpackget add <local_path>/Keil.B-U585I-IOT02A_BSP.pdsc`
    - [STM32U5xx_DFP 3.0.0-dev](https://github.com/Open-CMSIS-Pack/STM32U5xx_DFP)  
      Install pack: `cpackget add <local_path>/Keil.STM32U5xx_DFP.pdsc`
    - [CMSIS-Driver_STM32 1.0.0-dev0](https://github.com/Open-CMSIS-Pack/CMSIS-Driver_STM32)  
      Install pack: `cpackget add <local_path>/ARM.CMSIS-Driver_STM32.pdsc`
  - Target: NXP EVKB-IMXRT1050 Board (Mounted Device: MIMXRT1052DVL6B)
    - [IMXRT1050-EVKB_BSP 2.0.0-dev](https://github.com/Open-CMSIS-Pack/NXP_IMXRT1050-EVKB_BSP)  
      Install pack: `cpackget add <local_path>/Keil.IMXRT1050-EVKB_BSP.pdsc`
    - [CMSIS-Driver 2.9.0-dev](https://github.com/ARM-software/CMSIS-Driver)  
      Install pack: `cpackget add <local_path>/ARM.CMSIS-Driver.pdsc`
- CMSIS Packs - packs build from public repos and installed localy
  - Target: NXP EVKB-IMXRT1050 Board (Mounted Device: MIMXRT1052DVL6B)
    - [iMXRT105x_MWP 2.0.0-dev](https://github.com/Open-CMSIS-Pack/NXP_iMXRT105x_MWP)  
      Build pack: `gen_pack.sh`  
      Install pack: `cpackget add <local_path>/Keil.iMXRT105x_MWP.2.0.0-dev<n>.pack`
