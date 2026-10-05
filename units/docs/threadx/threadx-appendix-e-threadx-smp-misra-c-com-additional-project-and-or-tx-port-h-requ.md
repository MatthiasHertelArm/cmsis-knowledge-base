---
id: "threadx-appendix-e-threadx-smp-misra-c-com-additional-project-and-or-tx-port-h-requ"
type: "concept"
domain: "rtos"
title: "Appendix E - ThreadX SMP MISRA C compliance: MISRA C Overview / Additional Project and/or tx_port.h Requirements"
summary: "Some versions of ThreadX SMP may need additional configuration to achieve full MISRA compliance. In addition to building ThreadX SMP with TX_MISRA_ENABLE, the ThreadX project should have the C dialect C89 specified and strict language conformance selected, as follows:"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/appendix-e.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/appendix-e.md#additional-project-and-or-tx-port-h-requirements"
license: "MIT"
mode: "V"
---

_Part of: MISRA C Overview_

Some versions of ThreadX SMP may need additional configuration to
achieve full MISRA compliance. In addition to building ThreadX SMP with
**_TX_MISRA_ENABLE_**, the ThreadX project should have the C dialect C89
specified and strict language conformance selected, as follows:

(figure: Screenshot that shows strict language conformance.)

Next, if the version of ThreadX does not have a pre-built
**_tx_misra.s_** assembly file, the **_tx_misra.c_** file should be
compiled to assembly and the assembly file should be included in the
project.

Finally, **_tx_port.h_** should have the following changes for full
MISRA compliance:

1. The following defines should be present in **_tx_port.h_** or in the project settings:

   \#define TX_BLOCK_POOL_ENABLE_PERFORMANCE_INFO  
   \#define TX_BYTE_POOL_ENABLE_PERFORMANCE_INFO  
   \#define TX_EVENT_FLAGS_ENABLE_PERFORMANCE_INFO  
   \#define TX_MUTEX_ENABLE_PERFORMANCE_INFO  
   \#define TX_QUEUE_ENABLE_PERFORMANCE_INFO  
   \#define TX_SEMAPHORE_ENABLE_PERFORMANCE_INFO  
   \#define TX_THREAD_ENABLE_PERFORMANCE_INFO  
   \#define TX_TIMER_ENABLE_PERFORMANCE_INFO

2. The TX_DISABLE_NOTIFY_CALLBACKS should NOT be defined in **_tx_port.h_** or in the project settings.

3. TX_DISABLE_INLINE should be defined to disable the in-line helper functions in ThreadX SMP.

4. The trace timer source should be redefined as follows:

   \#ifndef TX_MISRA_ENABLE  
   \#ifndef TX_TRACE_TIME_SOURCE  
   \#define TX_TRACE_TIME_SOURCE /\* ORIGINAL SOURCE \*/  
   \#endif  
   \#else  
   ULONG \_tx_misra_time_stamp_get(VOID);  
   \#define TX_TRACE_TIME_SOURCE \_tx_misra_time_stamp_get()  
   \#endif

5. Change the in-line initialization option to (this also disables in-line assembly macros):

   \#ifdef TX_MISRA_ENABLE  
   \#define TX_DISABLE_INLINE  
   \#else  
   \#define TX_INLINE_INITIALIZATION  
   \#endif

6. Ensure that the disable stack checking option is disabled:
   \#ifndef TX_MISRA_ENABLE  
   \#ifdef TX_ENABLE_STACK_CHECKING  
   \#undef TX_DISABLE_STACK_FILLING  
   \#endif  
   \#endif
