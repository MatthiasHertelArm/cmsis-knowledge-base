---
id: "threadx-chapter-2-installation-and-use-of-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of ThreadX: Configuration Options"
summary: "There are several configuration options when building the ThreadX library and the application using ThreadX. The options below can be defined in the application source, on the command line, or within the tx_user.h include file."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter2.md#configuration-options"
license: "MIT"
mode: "V"
---

There are several configuration options when building the ThreadX library and the application using ThreadX. The options below can be defined in the application source, on the command line, or within the ***tx_user.h*** include file.

> **Important:** *Options defined in ***tx_user.h*** are applied only if the application and ThreadX library are built with **TX_INCLUDE_USER_DEFINE_FILE** defined.*

### Smallest Configuration

For the smallest code size, the following ThreadX configuration options should be considered (in absence of all other options).

```c
TX_DISABLE_ERROR_CHECKING
TX_DISABLE_PREEMPTION_THRESHOLD
TX_DISABLE_NOTIFY_CALLBACKS
TX_DISABLE_REDUNDANT_CLEARING
TX_DISABLE_STACK_FILLING
TX_NOT_INTERRUPTABLE
TX_TIMER_PROCESS_IN_ISR
```

### Fastest Configuration

For the fastest execution, the same configuration options used for the Smallest Configuration previously, but with these options also considered.

```c
TX_REACTIVATE_INLINE
TX_INLINE_THREAD_RESUME_SUSPEND
```

[Detailed configuration options](#detailed-configuration-options) are described.

### Global Time Source

For other Eclipse ThreadX products (FileX, NetX Duo, GUIX, USBX, etc.), ThreadX defines the number of ThreadX timer ticks that represents one second. Others derive their time requirements based on this constant. By default, the value is 100, assuming a 10ms periodic interrupt. The user may override this value by defining TX_TIMER_TICKS_PER_SECOND with the desired value in ***tx_port.h*** or within the IDE or command line.

### Detailed Configuration Options

**TX_BLOCK_POOL_ENABLE_PERFORMANCE_INFO**

When defined, this option enables the gathering of performance information on block pools. By default, this option is not defined.

**TX_BYTE_POOL_ENABLE_PERFORMANCE_INFO**

When defined, this option enables the gathering of performance information on byte pools. By default, this option is not defined.

**TX_DISABLE_ERROR_CHECKING**

Bypasses basic service call error checking. When defined in the application source, all basic parameter error checking is disabled. This may improve performance by as much as 30% and may also reduce the image size.

> **Note:** *It is only safe to disable error checking if the application can absolutely guarantee all input parameters are always valid under all circumstances, including input parameters derived from external input. If invalid input is supplied to the API with error checking disabled, the resulting behavior is undefined and could result in memory corruption or system crash.*

> **Note:** *ThreadX API return values not affected by disabling error checking are listed in bold in the "Return Values" section of each API description in Chapter 4. The nonbold return values are void if error checking is disabled by using the TX_DISABLE_ERROR_CHECKING option.*

**TX_DISABLE_NOTIFY_CALLBACKS**

When defined, disables the notify callbacks for various ThreadX objects. Using this option slightly reduces code size and improves performance. By default, this option is not defined.

**TX_DISABLE_PREEMPTION_THRESHOLD**

When defined, disables the preemption-threshold feature and slightly reduces code size and improves performance. Of course, the preemption-threshold capabilities are no longer available. By default, this option is not defined.

**TX_DISABLE_REDUNDANT_CLEARING**

When defined, removes the logic for initializing ThreadX global C data structures to zero. This should only be used if the compiler's initialization code sets all un-initialized C global data to zero. Using this option slightly reduces code size and improves performance during initialization. By default, this option is not defined.

**TX_DISABLE_STACK_FILLING**

When defined, disables placing the 0xEF value in each byte of each thread's stack when created. By default, this option is not defined.

**TX_ENABLE_EVENT_TRACE**

When defined, ThreadX enables the event gathering code for creating a TraceX trace buffer.

**TX_ENABLE_STACK_CHECKING**

When defined, enables ThreadX run-time stack checking, which includes analysis of how much stack has been used and examination of data pattern "fences" before and after the stack area. If a stack error is detected, the registered application stack error handler is called. This option does result in slightly increased overhead and code size. Review the ***tx_thread_stack_error_notify*** API function for more information. By default, this option is not defined.

**TX_EVENT_FLAGS_ENABLE_PERFORMANCE_INFO**

When defined, enables the gathering of performance information on event flags groups. By default, this option is not defined.

**TX_INLINE_THREAD_RESUME_SUSPEND**

When defined, ThreadX improves the ***tx_thread_resume*** and ***tx_thread_suspend*** API calls via in-line code. This increases code size but enhances performance of these two API calls.

**TX_MAX_PRIORITIES**

Defines the priority levels for ThreadX. Legal values range from 32 through 1024 (inclusive) and *must* be evenly divisible by 32. Increasing the number of priority levels supported increases the RAM usage by 128 bytes for every group of 32 priorities. However, there is only a negligible effect on performance. By default, this value is set to 32 priority levels.

**TX_MINIMUM_STACK**

Defines the minimum stack size (in bytes). It is used for error checking when threads are created. The default value is port-specific and is found in ***tx_port.h***.

**TX_MISRA_ENABLE**

When defined, ThreadX utilizes MISRA C compliant conventions. Refer to ***[ThreadX SMP MISRA C compliance](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/appendix-e.md)*** for details.

**TX_MUTEX_ENABLE_PERFORMANCE_INFO**

When defined, enables the gathering of performance information on mutexes. By default, this option is not defined.

**TX_NO_TIMER**

When defined, the ThreadX timer logic is completely disabled. This is useful in cases where the ThreadX timer features (thread sleep, API timeouts, time-slicing, and application timers) are not utilized. If **TX_NO_TIMER** is specified, the option **TX_TIMER_PROCESS_IN_ISR** must also be defined.

**TX_NOT_INTERRUPTABLE**

When defined, ThreadX does not attempt to minimize interrupt lockout time. This results in faster execution but does slightly increase interrupt lockout time.

**TX_QUEUE_ENABLE_PERFORMANCE_INFO**

When defined, enables the gathering of performance information on queues. By default, this option is not defined.

**TX_REACTIVATE_INLINE**

When defined, performs reactivation of ThreadX timers inline instead of using a function call. This improves performance but slightly increases code size. By default, this option is not defined.

**TX_SEMAPHORE_ENABLE_PERFORMANCE_INFO**

When defined, enables the gathering of performance information on semaphores. By default, this option is not defined.

**TX_THREAD_ENABLE_PERFORMANCE_INFO**

When defined, enables the gathering of performance information on threads. By default, this option is not defined.

**TX_TIMER_ENABLE_PERFORMANCE_INFO**

When defined, enables the gathering of performance information on timers. By default, this option is not defined.

**TX_TIMER_PROCESS_IN_ISR**

When defined, eliminates the internal system timer thread for ThreadX. This results in improved performance on timer events and smaller RAM requirements because the timer stack and control block are no longer needed. However, using this option moves all the timer expiration processing to the timer ISR level. By default, this option is not defined.

> **Note:** *Services allowed from timers may not be allowed from ISRs and thus might not be allowed when using this option.*

**TX_TIMER_THREAD_PRIORITY**

Defines the priority of the internal ThreadX system timer thread. The default value is priority 0—the highest priority in ThreadX. The default value is defined in ***tx_port.h***.

**TX_TIMER_THREAD_STACK_SIZE**

Defines the stack size (in bytes) of the internal ThreadX system timer thread. This thread processes all thread sleep requests as well as all service call timeouts. In addition, all application timer callback routines are invoked from this context. The default value is port-specific and is found in ***tx_port.h***.
