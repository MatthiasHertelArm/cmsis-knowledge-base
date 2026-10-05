---
id: "rtos2-process-isolation-handle-memory-access-faults"
type: "concept"
domain: "rtos"
title: "Process Isolation: Handle Memory Access Faults"
summary: "A memory access fault is triggered when a thread tries to access memory or peripherals outside of the MPU Protected Zone loaded while the thread is running."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md#handle-memory-access-faults"
license: "Apache-2.0"
mode: "V"
---

A memory access fault is triggered when a thread tries to access memory or peripherals outside of the MPU Protected Zone loaded while the thread is running. In such case Memory Management Interrupt [MemoryManagement_IRQn](https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/../Core/group__NVIC__gr.html) is triggered by the processor and its handling function is executed according to the exception vector table specified in the device startup file (by default `MemManage_Handler(void)` ).

The _MemManage_Handler()_ interrupt handler is application specific and needs to be implemented by the user. In the handler it is possible to identify the thread that caused the memory access fault, the corresponding zone id and the safety class. This information can be used to define actions for entering a safe state. rtos_process_isolation_faults provides more details on the available system recovery possibilities.

<!-- =============================================================== !-->
# Safety Classes

rtos_process_isolation_mpu_objects explains that MPU Protected Zones do not provide full access protection to RTOS objects accessed via CMSIS-RTOS2 API. The concept of a safety class fills this gap.

Every RTOS object, including thread is assigned with a numeric safety class value. A thread cannot modify an RTOS object if its safety class value is higher than the safety class value of the thread.
For example, it is not possible to change the priority or suspend a thread that has a higher safety class value than the thread that is currently executed.

**Function references**

 - Following functions and macros are used explicitly for managing safety classes:
   - osSafetyClass :  osSafetyClass
   - osThreadGetClass :  osThreadGetClass
   - osSafetyWithSameClass :  osSafetyWithSameClass
   - osSafetyWithLowerClass :  osSafetyWithLowerClass
   - osKernelProtect :  osKernelProtect
   - osThreadSuspendClass :  osThreadSuspendClass
   - osThreadResumeClass :  osThreadResumeClass
   - osKernelDestroyClass  :  osKernelDestroyClass
 - CMSIS-RTOS2 API functions that support safety class assignment when creating RTOS objects are listed in rtos_process_isolation_safety_class_assign.
 - CMSIS-RTOS2 API functions that verify safety class assignment before execution are listed in rtos_process_isolation_safety_class_error lists.
