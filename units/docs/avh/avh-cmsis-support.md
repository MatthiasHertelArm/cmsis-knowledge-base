---
id: "avh-cmsis-support"
type: "concept"
domain: "test"
title: "CMSIS Support"
summary: "Arm provides comprehensive CMSIS support for FVP targets in Open-CMSIS-Pack format, including device definitions, startup code, board support packages, and examples."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/simulation/src/avh_fvp_cmsis.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/simulation/src/avh_fvp_cmsis.md"
license: "Apache-2.0"
mode: "V"
---

Arm provides comprehensive CMSIS support for FVP targets in [Open-CMSIS-Pack format](https://www.open-cmsis-pack.org/), including device definitions, startup code, board support packages, and examples.

The following table lists available FVP models with their corresponding CMSIS-Packs and device names:



| Arm FVP Model Name | CMSIS Packs with DFP/BSP (1) | Device name | Description |
|---|---|---|---|
| FVP_Corstone_SSE-320 | [ARM.SSE_320_BSP](https://www.keil.arm.com/packs/sse_320_bsp-arm) | [`SSE-320-FVP`](https://www.keil.arm.com/devices/arm-sse-320-fvp) | Corstone-320 subsystem |
| FVP_Corstone_SSE-315 | [ARM.SSE_315_BSP](https://www.keil.arm.com/packs/sse_315_bsp-arm) | [`SSE-315-FVP`](https://www.keil.arm.com/devices/arm-sse-315-fvp) | Corstone-315 subsystem |
| FVP_Corstone_SSE-310 FVP_Corstone_SSE-310_Ethos-U65 | [ARM.V2M_MPS3_SSE_310_BSP](https://www.keil.arm.com/packs/v2m_mps3_sse_310_bsp-arm) | [`SSE-310-MPS3_FVP`](https://www.keil.arm.com/devices/arm-sse-310-mps3-fvp) | Corstone-310 subsystem |
| FVP_Corstone_SSE-300 FVP_Corstone_SSE-300_Ethos-U55 FVP_Corstone_SSE-300_Ethos-U65 | [ARM.V2M_MPS3_SSE_300_BSP](https://www.keil.arm.com/packs/v2m_mps3_sse_300_bsp-arm) | [`SSE-300-MPS3`](https://www.keil.arm.com/devices/arm-sse-300-mps3) | Corstone-300 subsystem |
| FVP_MPS2_Cortex-M85 | [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM85`](https://www.keil.arm.com/devices/arm-armcm85) | Generic Cortex-M85 device |
| FVP_MPS2_Cortex-M55 | [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM55`](https://www.keil.arm.com/devices/arm-armcm55) | Generic Cortex-M55 device |
| FVP_MPS2_Cortex-M52 | [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM52`](https://www.keil.arm.com/devices/arm-armcm52) | Generic Cortex-M52 device |
| FVP_MPS2_Cortex-M35P | [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM35P`](https://www.keil.arm.com/devices/arm-armcm35p) | Generic Cortex-M35P device |
| FVP_MPS2_Cortex-M33 | [Keil.V2M-MPS2_IOTKit_BSP](https://www.keil.arm.com/packs/v2m-mps2_iotkit_bsp-keil/) | [`IOTKit_CM33_VHT`](https://www.keil.arm.com/devices/arm-iotkit-cm33-vht) [`IOTKit_CM33_FP_VHT`](https://www.keil.arm.com/devices/arm-iotkit-cm33-vht) | Cortex-M33 IoT Kit subsystem |
| [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM33`](https://www.keil.arm.com/devices/arm-armcm33) | Generic Cortex-M33 device |  |
| FVP_MPS2_Cortex-M23 | [Keil.V2M-MPS2_IOTKit_BSP](https://www.keil.arm.com/packs/v2m-mps2_iotkit_bsp-keil/) | [`IOTKit_CM23_VHT`](https://www.keil.arm.com/devices/arm-iotkit-cm23-vht) | Cortex-M23 IoT Kit subsystem |
| [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM23`](https://www.keil.arm.com/devices/arm-armcm23) | Generic Cortex-M23 device |  |
| FVP_MPS2_Cortex-M7 | [Keil.V2M-MPS2_CMx_BSP](https://www.keil.arm.com/packs/v2m-mps2_cmx_bsp-keil) | [`CMSDK_CM7_VHT`](https://www.keil.arm.com/devices/arm-cmsdk-cm7-vht) [`CMSDK_CM7_SP_VHT`](https://www.keil.arm.com/devices/arm-cmsdk-cm7-sp-vht) [`CMSDK_CM7_DP_VHT`](https://www.keil.arm.com/devices/arm-cmsdk-cm7-dp-vht) | Cortex-M7 System Design Kit Device SP variant - Single Precision FPU support DP variant - Dual Precision FPU support |
| [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM7`](https://www.keil.arm.com/devices/arm-armcm7) | Generic Cortex-M7 device |  |
| FVP_MPS2_Cortex-M4 | [Keil.V2M-MPS2_CMx_BSP](https://www.keil.arm.com/packs/v2m-mps2_cmx_bsp-keil) | [`CMSDK_CM4_VHT`](https://www.keil.arm.com/devices/arm-cmsdk-cm4-vht) [`CMSDK_CM4_FP_VHT`](https://www.keil.arm.com/devices/arm-cmsdk-cm4-fp-vht) | Cortex-M3 System Design Kit Device FP variant - with Floating Point Unit (FPU) support |
| [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM4`](https://www.keil.arm.com/devices/arm-armcm4) | Generic Cortex-M4 device |  |
| FVP_MPS2_Cortex-M3 | [Keil.V2M-MPS2_CMx_BSP](https://www.keil.arm.com/packs/v2m-mps2_cmx_bsp-keil) | [`CMSDK_CM3_VHT`](https://www.keil.arm.com/devices/arm-cmsdk-cm3-vht) | Cortex-M3 System Design Kit Device |
| [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM3`](https://www.keil.arm.com/devices/arm-armcm3) | Generic Cortex-M3 device |  |
| FVP_MPS2_Cortex-M0plus | [Keil.V2M-MPS2_CMx_BSP](https://www.keil.arm.com/packs/v2m-mps2_cmx_bsp-keil) | [`CMSDK_CM0plus_VHT`](https://www.keil.arm.com/devices/arm-cmsdk-cm0plus-vht) | Cortex-M0+ System Design Kit Device |
| [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM0plus`](https://www.keil.arm.com/devices/arm-armcm0plus) | Generic Cortex-M0+ device |  |
| FVP_MPS2_Cortex-M0 | [Keil.V2M-MPS2_CMx_BSP](https://www.keil.arm.com/packs/v2m-mps2_cmx_bsp-keil) | [`CMSDK_CM0_VHT`](https://www.keil.arm.com/devices/arm-cmsdk-cm0-vht) | Cortex-M0 System Design Kit Device |
| [ARM.Cortex_DFP](https://www.keil.arm.com/packs/cortex_dfp-arm) | [`ARMCM0`](https://www.keil.arm.com/devices/arm-armcm0) | Generic Cortex-M0 device |  |



**Note:** (1) BSP packs (suffixed with "_BSP") include both board support and device definitions, eliminating the need for a separate Device Family Pack (DFP).
