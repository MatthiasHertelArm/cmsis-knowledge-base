---
id: "threadx-chapter-2-installation-use-of-thre-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation & Use of ThreadX SMP: Configuration Options"
summary: "There are several configuration options when building the ThreadX SMP library and the application using ThreadX SMP. The options below can be defined in the application source, on the command line, or within the tx_user.h include file."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter2.md#configuration-options"
license: "MIT"
mode: "V"
---

There are several configuration options when building the ThreadX SMP library and the application using ThreadX SMP. The options below can be defined in the application source, on the command line, or within the ***tx_user.h*** include file.

> **Important:** Options defined in **tx_user.h** are applied only if the application and ThreadX SMP library are built with **TX_INCLUDE_USER_DEFINE_FILE** defined.

### Smallest Configuration
For the smallest code size, the following ThreadX SMP configuration options should be considered (in absence of all other options):

- TX_DISABLE_ERROR_CHECKING
- TX_DISABLE_PREEMPTION_THRESHOLD
- TX_DISABLE_NOTIFY_CALLBACKS 
- TX_DISABLE_REDUNDANT_CLEARING 
- TX_DISABLE_STACK_FILLING 
- TX_NOT_INTERRUPTABLE 
- TX_TIMER_PROCESS_IN_ISR

### Fastest Configuration 
For the fastest execution, the same configuration options used for the Smallest Configuration previously, but with this option also considered:

- TX_REACTIVATE_INLINE

Review the ***readme_threadx.txt*** file for additional options for your specific version of ThreadX SMP. Detailed configuration options are described beginning on page 28.

### Global Time Source  
For other Eclipse ThreadX products (FileX, NetX Duo, GUIX, USBX, etc.), ThreadX SMP defines the number of ThreadX SMP timer ticks that represents one second. Others derive their time requirements based on this constant. By default, the value is 100, assuming a 10ms periodic interrupt. The user may override this value by defining TX_TIMER_TICKS_PER_SECOND with the desired value in ***tx_port.h*** or within the IDE or command line.

### Detailed Configuration Options

- **TX_BLOCK_POOL_ENABLE_PERFORMANCE_INFO** : When defined, enables the gathering of performance information on block pools. By default, this option is not defined.
- **TX_BYTE_POOL_ENABLE_PERFORMANCE_INFO** : When defined, enables the gathering of performance information on byte pools. By default, this option is not defined.
- **TX_DISABLE_ERROR_CHECKING**: Bypasses basic service call error checking. When defined in the application source, all basic parameter error checking is disabled. This may improve performance by as much as 30% and may also reduce the image size.

> **Note:** *It is only safe to disable error checking if the application can absolutely guarantee all input parameters are always valid under all circumstances, including input parameters derived from external input. If invalid input is supplied to the API with error checking disabled, the resulting behavior is undefined and could result in memory corruption or system crash.*

> **Note:** *ThreadX SMP API return values not affected by disabling error checking are listed in bold in the "Return Values" section of each API description in Chapter 4. The nonbold return values are void if error checking is disabled by using the TX_DISABLE_ERROR_CHECKING option.*
- **TX_DISABLE_NOTIFY_CALLBACKS** : When defined, disables the notify callbacks for various ThreadX SMP objects. Using this option slightly reduces code size and improves performance. By default, this option is not defined.
- **TX_DISABLE_PREEMPTION_THRESHOLD** : When defined, disables the preemption threshold feature and slightly reduces code size and improves performance. Of course, the preemption threshold capabilities are no longer available. By default, this option is not defined.
- **TX_DISABLE_REDUNDANT_CLEARING** : When defined, removes the logic for initializing ThreadX SMP global C data structures to zero. This should only be used if the compiler's initialization code sets all un-initialized C global data to zero. Using this option slightly reduces code size and improves performance during initialization. By default, this option is not defined.
- **TX_DISABLE_STACK_FILLING** : When defined, disables placing the 0xEF value in each byte of each thread's stack when created. By default, this option is not defined.
- **TX_ENABLE_EVENT_TRACE** : When defined, ThreadX SMP enables the event gathering code for creating a TraceX trace buffer. See the TraceX User Guide for more details.
- **TX_ENABLE_STACK_CHECKING** : When defined, enables ThreadX SMP run-time stack checking, which includes analysis of how much stack has been used and examination of data pattern "fences" before and after the stack area. If a stack error is detected, the registered application stack error handler is called. This option does result in slightly increased overhead and code size. Review the ***tx_- thread_stack_error_notify*** API for more information. By default, this option is not defined.
- **TX_EVENT_FLAGS_ENABLE_PERFORMANCE_INFO** : When defined, enables the gathering of performance information on event flags groups. By default, this option is not defined.
- **TX_INLINE_THREAD_RESUME_SUSPEND** : When defined, ThreadX SMP improves the ***tx_thread_resume*** and ***tx_thread_suspend*** API calls via in-line code. This increases code size but enhances performance of these two API calls.
- **TX_MAX_PRIORITIES** : Defines the priority levels for ThreadX SMP. Legal values range from 32 through 1024 (inclusive) and must be evenly divisible by 32. Increasing the number of priority levels supported increases the RAM usage by 128 bytes for every group of 32 priorities. However, there is only a negligible effect on performance. By default, this value is set to 32 priority levels.
- **TX_MINIMUM_STACK** : Defines the minimum stack size (in bytes). It is used for error checking when threads are created. The default value is port-specific and is found in ***tx_port.h.***
- **TX_MISRA_ENABLE** : When defined, ThreadX SMP utilizes MISRA C compliant conventions. Refer to ***[ThreadX SMP MISRA C compliance](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/appendix-e.md)*** for details.
- **TX_MUTEX_ENABLE_PERFORMANCE_INFO** : When defined, enables the gathering of performance information on mutexes. By default, this option is not defined.
- **TX_NO_TIMER** : When defined, the ThreadX SMP timer logic is completely disabled. This is useful in cases where the ThreadX SMP timer features (thread sleep, API timeouts, time-slicing, and application timers) are not utilized.
- **TX_NOT_INTERRUPTABLE** : When defined, ThreadX SMP does not attempt to minimize interrupt lockout time. This results in faster execution but does slightly increase interrupt lockout time.
- **TX_QUEUE_ENABLE_PERFORMANCE_INFO** : When defined, enables the gathering of performance information on queues. By default, this option is not defined.
- **TX_REACTIVATE_INLINE** : When defined, performs reactivation of ThreadX SMP timers in-line instead of using a function call. This improves performance but slightly increases code size. By default, this option is not defined.
- **TX_SEMAPHORE_ENABLE_PERFORMANCE_INFO** : When defined, enables the gathering of performance information on semaphores. By default, this option is not defined.
- **TX_THREAD_ENABLE_PERFORMANCE_INFO** : When defined, enables the gathering of performance information on threads. By default, this option is not defined.
- **TX_THREAD_SMP_CORE_MASK** : Defines bit map mask for CORE exclusion. For example, a 4-core environment has a value of 0xF for this define.
- **TX_THREAD_SMP_DEBUG_ENABLE** : When defined, ThreadX SMP debug information is saved in a circular buffer.
- **TX_THREAD_SMP_DYNAMIC_CORE_MAX** : When defined, enables the dynamic maximum number of cores that can be adjusted at run-time.
- **TX_THREAD_SMP_EQUAL_PRIORITY** : When defined, ThreadX SMP only schedules equal priority threads in parallel. This should be defined prior to building the ThreadX SMP library.
- **TX_THREAD_SMP_INTER_CORE_INTERRUPT** : When defined, ThreadX SMP generates inter-core interrupts.
- **TX_THREAD_SMP_MAX_CORES** : Defines the maximum number of cores.
- **TX_THREAD_SMP_ONLY_CORE_0_DEFAULT** : When defined, ThreadX SMP defaults all threads and timers to execute only on core 0 by default. The application may override this by calling the core exclude APIs. This should be defined prior to building the ThreadX SMP library.
- **TX_THREAD_SMP_WAKEUP_LOGIC** : When defined, application macro to wakeup core "i" is invoked. This should be defined prior to inclusion of ***tx_port.h.***
- **TX_THREAD_SMP_WAKEUP(i)** : Defines an application macro to wakeup core "i". This should be defined prior to inclusion of ***tx_port.h.***
- **TX_TIMER_ENABLE_PERFORMANCE_INFO** : When defined, enables the gathering of performance information on timers. By default, this option is not defined.
- **TX_TIMER_PROCESS_IN_ISR** : When defined, eliminates the internal system timer thread for ThreadX SMP. This results in improved performance on timer events and smaller RAM requirements because the timer stack and control block are no longer needed. However, using this option moves all the timer expiration processing to the timer ISR level. By default, this option is not defined.

  > **Note:** That services allowed from timers may not be allowed from ISRs and thus might not be allowed when using this option.

- **TX_TIMER_THREAD_PRIORITY** : Defines the priority of the internal ThreadX SMP system timer thread. The default value is priority 0—the highest priority in ThreadX SMP. The default value is defined in ***tx_port.h.***
- **TX_TIMER_THREAD_STACK_SIZE** : Defines the stack size (in bytes) of the internal ThreadX SMP system timer thread. This thread processes all thread sleep requests as well as all service call timeouts. In addition, all application timer callback routines are invoked from this context. The default value is port-specific and is found in ***tx_port.h.***
