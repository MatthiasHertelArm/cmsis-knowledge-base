---
id: "threadx-chapter-2-installation-and-use-of-using-threadx"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of ThreadX: Using ThreadX"
summary: "To use ThreadX, the application code must include tx_api.h during compilation and link with the ThreadX run-time library tx.a (or tx.lib)."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter2.md#using-threadx"
license: "MIT"
mode: "V"
---

To use ThreadX, the application code must include ***tx_api.h*** during compilation and link with the ThreadX run-time library ***tx.a*** (or ***tx.lib***).

There are four steps required to build a ThreadX application.

1. Include the ***tx_api.h*** file in all application files that use ThreadX services or data structures.

1. Create the standard C ***main*** function. This function must eventually call ***tx_kernel_enter*** to start ThreadX. Application-specific initialization that does not involve ThreadX may be added prior to entering the kernel.

   > **Important:** *The ThreadX entry function ***tx_kernel_enter*** does not return. So be sure not to place any processing or function calls after it.*

1. Create the ***tx_application_define*** function. This is where the initial system resources are created. Examples of system resources include threads, queues, memory pools, event flags groups, mutexes, and semaphores.

1. Compile application source and link with the ThreadX run-time library ***tx.lib***. The resulting image can be downloaded to the target and executed!
