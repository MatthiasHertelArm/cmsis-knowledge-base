---
id: "rtos2-mainpage-supported-rtos-kernels"
type: "concept"
domain: "rtos"
title: "mainpage: Supported RTOS kernels"
summary: "Many popular RTOS kernels include support for CMSIS-RTOS2 API:"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/mainpage.md#supported-rtos-kernels"
license: "Apache-2.0"
mode: "V"
---

Many popular RTOS kernels include support for CMSIS-RTOS2 API:

**CMSIS-RTX** (or Keil RTX5): provides most complete support for CMSIS-RTOS2 API and uses it as native interface. For more information see:

 - [CMSIS-RTX GitHub repository](https://github.com/ARM-software/CMSIS-RTX)
 - [CMSIS-RTX documentation](https://arm-software.github.io/CMSIS-RTX/)
 - [CMSIS-RTX pack](https://www.keil.arm.com/packs/cmsis-rtx-arm/versions/)

**FreeRTOS** : this popular RTOS kernel is enabled with CMSIS-RTOS2 API in the *CMSIS-FreeRTOS* variant. To learn more see:

 - [CMSIS-FreeRTOS GitHub repository](https://github.com/ARM-software/CMSIS-FreeRTOS)
 - [CMSIS-FreeRTOS documentation](https://arm-software.github.io/CMSIS-FreeRTOS/)
 - [CMSIS-FreeRTOS pack](https://www.keil.arm.com/packs/cmsis-freertos-arm/versions/)

**Zephyr RTOS**: is developed under governance of Linux Foundation and includes CMSIS-RTOS2 API support. See more at:

 - [Zephyr GitHub repository](https://github.com/zephyrproject-rtos/zephyr), see folder *subsys/portability/cmsis_rtos_v2/*
 - [Zephyr documentation about CMSIS-RTOS2 support](https://docs.zephyrproject.org/latest/services/portability/cmsis_rtos_v2.html)

**embOS**: is a preemptive RTOS designed by Segger, and provides support for CMSIS-RTOS2 API.

 - [Using embOS in CMSIS-Pack projects](https://wiki.segger.com/Using_embOS_in_CMSIS-Pack_projects)
 - [CMSIS-embOS pack](https://www.keil.arm.com/packs/cmsis-embos-segger/versions/)

**Azure ThreadX RTOS for STM32**: is an integration of Azure RTOS into STM32 middleware provided by STMicroelectronics.

 - [CMSIS-RTOS API support in ThreadX for STM32](https://wiki.st.com/stm32mcu/wiki/Introduction_to_THREADX#CMSIS-RTOS_API_Support)

**Micrium OS** is developed and maintained by Silicon Labs.

 - [Micrium OS overview and comparison](https://www.silabs.com/developers/rtos)
