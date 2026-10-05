---
id: "rtx-configure-rtx-v5-system-configuration"
type: "concept"
domain: "rtos"
title: "Configure RTX v5: System Configuration"
summary: "The system configuration covers system-wide settings for the global memory pool, tick frequency, ISR event buffer and round-robin thread switching."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/configure.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/configure.md#system-configuration"
license: "Apache-2.0"
mode: "V"
---

The system configuration covers system-wide settings for the global memory pool, tick frequency, ISR event buffer and
round-robin thread switching.

**System Configuration Options**

(figure: RTX_Config.h: System Configuration)

Name                               | \#define                 | Description
-----------------------------------|--------------------------|----------------------------------------------------------------
systemConfig_glob_mem         | `OS_DYNAMIC_MEM_SIZE`    | Defines the combined global dynamic memory size for the GlobalMemoryPool. Default value is `32768`. Value range is `[0-1073741824]` bytes, in multiples of `8` bytes.
Kernel Tick Frequency (Hz)         | `OS_TICK_FREQ`           | Defines base time unit for delays and timeouts in Hz. Default value is `1000` (1000 Hz = 1 ms period).
systemConfig_rr               | `OS_ROBIN_ENABLE`        | Enables Round-Robin Thread switching. Default value is `1` (enabled).
Round-Robin Timeout                | `OS_ROBIN_TIMEOUT`       | Defines how long a thread will execute before a thread switch. Default value is `5`. Value range is `[1-1000]`.
safetyConfig_safety           | `OS_SAFETY_FEATURES`     | Enables safety-related features as configured in this group. Default value is `1` (enabled).
Safety class                       | `OS_SAFETY_CLASS`        | Enables rtos_process_isolation_safety_class functionality. Default value is `1` (enabled).
MPU Protected Zone                 | `OS_EXECUTION_ZONE`      | Enables rtos_process_isolation_mpu. Default value is `1` (enabled).
Thread Watchdog                    | `OS_THREAD_WATCHDOG`     | Enables rtos_process_isolation_thread_wdt functionality. Default value is `1` (enabled).
Object Pointer checking            | `OS_OBJ_PTR_CHECK`       | Enables verification of object pointer alignment and memory region. Default value is `0` (disabled).
SVC Function Pointer checking      | `OS_SVC_PTR_CHECK`       | Enables verification of SVC function pointer alignment and memory region. Default value is `0` (disabled).
systemConfig_isr_fifo         | `OS_ISR_FIFO_QUEUE`      | RTOS Functions called from ISR store requests to this buffer. Default value is `16 entries`. Value range is `[4-256]` entries in multiples of `4`.
systemConfig_usage_counters   | `OS_OBJ_MEM_USAGE`       | Enables object memory usage counters to evaluate the maximum memory pool requirements individually for each RTOS object type. Default value is `0` (disabled).

### Global Dynamic Memory size [bytes]

Refer to GlobalMemoryPool.

### Round-Robin Thread Switching

RTX5 may be configured to use round-robin multitasking thread switching. Round-robin allows quasi-parallel execution of several threads of the _same_ priority. Threads are not really executed concurrently, but are scheduled where the available CPU time is divided into time slices and RTX5 assigns a time slice to each thread. Because the time slice is typically short (only a few milliseconds), it appears as though threads execute simultaneously.

Round-robin thread switching functions as follows:

- the tick is preloaded with the timeout value when a thread switch occurs
- the tick is decremented (if not already zero) each system tick if the same thread is still executing
- when the tick reaches 0 it indicates that a timeout has occurred. If there is another thread ready with the *same* priority, then the system switches to that thread and the tick is preloaded with timeout again.

In other words, threads execute for the duration of their time slice (unless a thread's time slice is given up). Then, RTX switches to the next thread that is in **READY** state and has the same priority. If no other thread with the same priority is ready to run, the current running thread resumes it execution.

Round-Robin multitasking is controlled with the `#define OS_ROBIN_ENABLE`. The time slice period is configured (in RTX timer ticks) with the `#define OS_ROBIN_TIMEOUT`.

### Safety features (Source variant only)

Safety features group in systemConfig enables individual selection of safety-related functionalities. It requires that RTX is used in the source variant.

It also includes:

- Thread functions: osThreadProtectPrivileged

**MPU Protected Zone**

Enables rtos_process_isolation_mpu functionality in the system. This includes:

- Thread attributes: osThreadZone
- Thread functions: osThreadGetZone, osThreadTerminateZone
- Zone Management: osZoneSetup_Callback

When enabled, the MPU Protected Zone values also need to be specified for the threads created by the kernel:

- For Idle thread in threadConfig
- For Timer thread in timerConfig

**Safety class**

Enables rtos_process_isolation_safety_class functionality in the system RTOS. This includes:

- Object attributes: osSafetyClass
- Kernel functions: osKernelProtect, osKernelDestroyClass
- Thread functions: osThreadGetClass, osThreadSuspendClass, osThreadResumeClass

When enabled, the safety class values need to be specified for threads created  by the kernel:

- For Idle thread in threadConfig
- For Timer thread in timerConfig

**Thread Watchdog**

Enables rtos_process_isolation_thread_wdt functionality in the system RTOS. This includes:

- Thread functions: osThreadFeedWatchdog
- Handler functions: osWatchdogAlarm_Handler

**Object Pointer checking**

Enables verification of object pointer alignment and memory region.

Before accessing RTX objects the RTX kernel verifies that obtained object pointer is valid (at least not `NULL`). When *Object Pointer checking* is enabled the kernel will additionally verify that the control block of the object is located in the memory section allocated for such object type, and that it is correctly aligned within that memory section.

If static memory allocation is used, the user shall place the control blocks of the objects into the correct named memory sections as described in StaticObjectMemory.

For object-specific and dynamic memory allocations the kernel will place the objects correctly.

**SVC Function Pointer checking**

Enables verification of SVC function pointer alignment and memory region.

Many kernel functions are executed in SVC context. Corresponding function pointers are placed by the kernel into a special named memory section. If *SVC Function Pointer checking* is enabled the kernel before calling an SVC function will additionally verify that its pointer is located in the expected memory section and is correctly aligned within that memory region.

### ISR FIFO Queue

The RTX functions (CMSIS_RTOS_ISR_Calls), when called from and interrupt handler, store the request type and optional parameter to the ISR FIFO queue buffer to be processed later, after the interrupt handler exits.

The scheduler is activated immediately after the IRQ handler has finished its execution to process the requests stored to the FIFO queue buffer. The required size of this buffer depends on the number of functions that are called within the interrupt handler. An insufficient queue size will be caught by osRtxErrorNotify with error code osRtxErrorISRQueueOverflow.

### Object Memory Usage Counters

Object memory usage counters help to evaluate the maximum memory pool requirements for each object type, just like stack watermarking does for threads. The initial setup starts with a global memory pool for all object types. Consecutive runs of the application with object memory usage counters enabled, help to introduce object specific memory pools for each object type. Normally, this is required for applications that require a functional safety certification as global memory pools are not allowed in this case.
