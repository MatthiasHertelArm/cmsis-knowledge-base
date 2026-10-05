---
id: "alp-project-migration-cmsis-v6-device-mapping-device-mapping"
type: "concept"
domain: "project"
title: "Migrating Projects to CMSIS v6: Device mapping: Device mapping"
summary: "If you are using an Arm device from the CMSIS v5 pack, you need to switch the device selection to one of the supported devices in the new Cortex_DFP pack. The following table shows the available mappings:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/project-migration-cmsis-v6/device_mapping.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/project-migration-cmsis-v6/device_mapping/#device-mapping"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you are using an Arm device from the CMSIS v5 pack, you need to switch the device selection to one of the supported devices in the new Cortex_DFP pack. The following table shows the available mappings:

| CMSIS v5                                                   | Cortex_DFP |
|------------------------------------------------------------|-----------|
| ARMCM0                                                     | ARMCM0 (NO_FPU, NO_MPU) |
| ARMCM0P, ARMCM0P_MPU                                       | ARMCM0P (NO_FPU, MPU) |
| ARMCM1                                                     | ARMCM1 (NO_FPU, NO_MPU) |
| ARMCM3                                                     | ARMCM3 (NO_FPU, MPU) |
| ARMCM4, ARMCM4_FP                                          | ARMCM4 (SP_FPU, MPU) |
| ARMCM7, ARMCM7_SP, ARMCM7_DP                               | ARMCM7 (DP_FPU, MPU) |
| ARMCM23, ARMCM23_TZ                                        | ARMCM23 (NO_FPU, MPU, TZ) |
| ARMCM33, ARMCM33_TZ, ARMCM33_DSP_FP, ARMCM33_DSP_FP_TZ     | ARMCM33 (SP_FPU, MPU, DSP, TZ) |
| ARMCM35P, ARMCM35P_TZ, ARMCM35P_DSP_FP, ARMCM35P_DSP_FP_TZ | ARMCM35P (SP_FPU, MPU, DSP, TZ) |
| ARMCM55                                                    | ARMCM55 (DP_FPU, MPU, FP_MVE, DSP, TZ) |
| ARMCM85                                                    | ARMCM85 (PACBTI, MPU, DP_FPU, FP_MVE, DSP, TZ) |
| ARMSC000                                                   | ARMSC000 (NO_FPU, NO_MPU) |
| ARMSC300                                                   | ARMSC300 (NO_FPU, NO_MPU) |
| ARMv8MBL                                                   | ARMCM23 (NO_FPU, MPU, TZ) |
| ARMv8MML, ARMv8MML_DSP, ARMv8MML_SP, ARMv8MML_DSP_SP, ARMv8MML_DP, ARMv8MML_DSP_DP | ARMCM33 (SP_FPU, MPU, DSP, TZ) |
| ARMv81MML_DSP_DP_MVE_FP                                    | ARMCM55 (DP_FPU, MPU, FP_MVE, DSP, TZ) |

**Note:**
To reduce the functionality of the new device mappings, use the appropriate compiler flags. Please consult the toolchain manual for the compiler flags.
