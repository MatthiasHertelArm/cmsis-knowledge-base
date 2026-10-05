---
id: "rtx-system-requirements-stack-requirements"
type: "concept"
domain: "rtos"
title: "System Requirements: Stack Requirements"
summary: "Keil RTX v5 kernel functions are executed in handler mode (using PendSV/SysTick/SVC) and the table below lists the maximum stack requirements for the Main Stack (MSP) that the user should consider."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/system_reqs.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/system_reqs.md#stack-requirements"
license: "Apache-2.0"
mode: "V"
---

Keil RTX v5 kernel functions are executed in handler mode (using PendSV/SysTick/SVC) and the table below lists the maximum stack requirements for the Main Stack (MSP) that the user should consider.

The stack for the osKernelStart function is referred as "Startup" and RTX v5 uses 32 bytes (with Arm Compiler). However the user should also consider additional stack that might be allocated by the `main` function of the embedded application. The following picture shows a worst-case memory allocation of the Main Stack.

(figure: Main Stack usage of RTX v5 applications)

The stack requirements depend on the compiler and the optimization level. RTX v5 supports event annotations and this configuration impacts also the stack requirement.

Application note [KAN316: Determining the stack usage of applications](https://developer.arm.com/documentation/kan316/latest/) describes the stack usage in RTX applications , explains how to analyze actual stack consumption and find the optimal setting.

\ifnot FuSaRTS
**Arm Compiler ARMCC V6.20**: Main Stack requirements for PendSV/SysTick/SVC

Optimization         | RTX Kernel  | RTX Kernel + Event Recorder
:--------------------|:------------|:--------------------------------
-O1 (Debug)          |  96 bytes   | 224 bytes
-Os (Balanced)       | 100 bytes   | 232 bytes
-Oz (Size)           | 104 bytes   | 248 bytes

\endif
