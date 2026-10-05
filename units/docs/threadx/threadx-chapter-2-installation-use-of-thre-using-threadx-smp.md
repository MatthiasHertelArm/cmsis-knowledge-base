---
id: "threadx-chapter-2-installation-use-of-thre-using-threadx-smp"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation & Use of ThreadX SMP: Using ThreadX SMP"
summary: "Using ThreadX SMP is easy. Basically, the application code must include tx_api.h during compilation and link with the ThreadX SMP run-time library tx.a (or tx.lib)."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter2.md#using-threadx-smp"
license: "MIT"
mode: "V"
---

Using ThreadX SMP is easy. Basically, the application code must include ***tx_api.h*** during compilation and link with the ThreadX SMP run-time library ***tx.a*** (or ***tx.lib)***.

There are four steps required to build a ThreadX SMP application:

Include the ***tx_api.h*** file in all application files that use ThreadX SMP services or data structures.

Create the standard C ***main*** function. This function must eventually call ***tx_kernel_enter*** to start ThreadX SMP. Application-specific initialization that does not involve ThreadX SMP may be added prior to entering the kernel.

> **Important:** The ThreadX SMP entry function **tx_kernel_enter** does not return. So be sure not to place any processing or function calls after it.

Create the ***tx_application_define*** function. This is where the initial system resources are created. Examples of system resources include threads, queues, memory pools, event flags groups, mutexes, and semaphores.

Compile application source and link with the ThreadX SMP run-time library ***tx.lib***. The resulting image can be downloaded to the target and executed!
