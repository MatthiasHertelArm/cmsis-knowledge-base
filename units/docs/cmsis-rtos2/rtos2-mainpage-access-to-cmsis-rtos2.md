---
id: "rtos2-mainpage-access-to-cmsis-rtos2"
type: "concept"
domain: "rtos"
title: "mainpage: Access to CMSIS-RTOS2"
summary: "CMSIS-RTOS2 and OS Tick intefaces are actively maintained in the CMSIS 6 GitHub repository and provided as part of the CMSIS Software Pack."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/mainpage.md#access-to-cmsis-rtos2"
license: "Apache-2.0"
mode: "V"
---

CMSIS-RTOS2 and OS Tick intefaces are actively maintained in the [**CMSIS 6 GitHub repository**](https://github.com/ARM-software/CMSIS_6) and provided as part of the [**CMSIS Software Pack**](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/../General/cmsis_pack.html).

The following files and directories relevant to CMSIS-RTOS2 are present in the **ARM::CMSIS** Pack:

File/Directory                        | Content
:-------------------------------------|:----------------------------------------------------
📂 CMSIS                              | CMSIS Base software components folder
 ┣ 📂 Documentation/html/RTOS2        | A local copy of this CMSIS-RTOS2 documentation
 ┗ 📂 RTOS2                           | CMSIS-RTOS2 API header files and OS tick implementations
   ┣ 📂 Include             | API header files
    ┣ 📄 cmsis_os2.h    | cmsis_os2_h
    ┗ 📄 os_tick.h      | CMSIS_RTOS_TickAPI header file
   ┗ 📂 Source               | OS tick implementations
    ┣ 📄 os_systick.c   | OS tick implementation using Cortex-M SysTick timer
    ┣ 📄 os_tick_gtim.c | OS tick implementation using Cortex-A Generic Timer
    ┗ 📄 os_tick_ptim.c | OS tick implementation using Cortex-A Private Timer
