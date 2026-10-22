---
id: "rtos2-process-isolation"
type: "concept"
domain: "rtos"
title: "Process Isolation"
summary: "CMSIS-RTOS2 API supports a concept of process isolation that allows developers to protect execution of critical software tasks against potential flaws in other parts of a program."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md"
license: "Apache-2.0"
mode: "V"
---

CMSIS-RTOS2 API supports a concept of **process isolation** that allows developers to protect execution of critical software tasks against potential flaws in other parts of a program.

Process Isolation in CMSIS-RTOS2 is enabled by following features:

 - rtos_process_isolation_mpu for memory access protection in the system using Memory Protection Unit (MPU).

    RTOS threads are executed with permission to access only memory regions and peripherals required for their operation. Hence thread code cannot accidentally modify critical RTOS kernel data or memory dedicated to other tasks.
 .
 - rtos_process_isolation_safety_class for access protection to RTOS objects via RTOS APIs.

    The RTOS objects with a higher safety class assigned to them cannot be modified via RTOS API functions from threads that have lower safety class assigned.
 .
 - rtos_process_isolation_thread_wdt to verify execution times of threads.

    Each thread can maintain own thread watchdog and in case of timing violations, corresponding thread watchdog alarm will be triggered.
 .
 - rtos_process_isolation_faults in case of a detected failure (for example thread watchdog alarm or MPU Fault).

    The RTOS provides functions to block execution of malfunctioning components and with that dedicate system resources for operation of the safety critical threads.

\if FuSaRTS
Section fusa_process_isolation lists safety requirements for Process Isolation functions.
\endif

<!-- =============================================================== !-->
# MPU Protected Zones

Memory Protection Unit (MPU) is available on many Cortex-M devices and allows to execute code with restricted access to memory regions and peripherals. Detailed information about the MPU can be found in [Cortex-M Reference Manuals](https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/../Core/index.html#ref_man_sec).

CMSIS-RTOS2 provides a concept of **MPU Protected Zones** as a simple and flexible mechanism for using MPUs with RTOS threads. MPU Protected Zones are defined by a user as a set of memory regions and peripherals with specified access rights, and each RTOS threads gets assigned to a specific MPU Protected Zone that it is allowed to use.

The figure below illustrates the concept for MPU Protected Zones for isolating threads.

(figure: System partitioning with MPU Protected Zones)

Sections below explain in details how to define and use MPU Protected Zones:

 - rtos_process_isolation_mpu_def
 - rtos_process_isolation_mpu_load
 - rtos_process_isolation_mpu_objects
 - rtos_process_isolation_mpu_fault

**Function references**

Following functions implement and use MPU Protected Zone functionality:

 - osThreadNew :  osThreadNew
 - osThreadZone :  osThreadZone
 - osThreadGetZone :  osThreadGetZone
 - osThreadTerminateZone :  osThreadTerminateZone
 - osZoneSetup_Callback :  osZoneSetup_Callback
