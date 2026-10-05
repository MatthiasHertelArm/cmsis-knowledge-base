---
id: "threadx-chapter-3-functional-components-of-initialization"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Initialization"
summary: "Understanding the initialization process is important. The initial hardware environment is set up here. In addition, this is where the application is given its initial personality."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#initialization"
license: "MIT"
mode: "V"
---

Understanding the initialization process is important. The initial hardware environment is set up here. In addition, this is where the application is given its initial personality.

> **Note:** *ThreadX attempts to utilize (whenever possible) the complete development tool's initialization process. This makes it easier to upgrade to new versions of the development tools in the future.*

### System Reset Vector

All microprocessors have reset logic. When a reset occurs (either hardware or software), the address of the application's entry point is retrieved from a specific memory location. After the entry point is retrieved, the processor transfers control to that location. The application entry point is quite often written in the native assembly language and is usually supplied by the development tools (at least in template form). In some cases, a special version of the entry program is supplied with ThreadX.

### Development Tool Initialization

After the low-level initialization is complete, control transfers to the development tool's high-level initialization. This is usually the place where initialized global and static C variables are set up. Remember their initial values are retrieved from the constant area. Exact initialization processing is development tool specific.

### main Function

When the development tool initialization is complete, control transfers to the user-supplied *main* function. At this point, the application controls what happens next. For most applications, the main function simply calls *tx_kernel_enter*, which is the entry into ThreadX. However, applications can perform preliminary processing (usually for hardware initialization) prior to entering ThreadX.

> **Important:** *The call to tx_kernel_enter does not return, so do not place any processing after it.*

### tx_kernel_enter

The entry function coordinates initialization of various internal ThreadX data structures and then calls the application's definition function ***tx_application_define***.

When ***tx_application_define*** returns, control is transferred to the thread scheduling loop. This marks the end of initialization.

### Application Definition Function

The ***tx_application_define*** function defines all of the initial application threads, queues, semaphores, mutexes, event flags, memory pools, and timers. It is also possible to create and delete system resources from threads during the normal operation of the application. However, all initial application resources are defined here.

The ***tx_application_define*** function has a single input parameter and it is certainly worth mentioning. The *first-available* RAM address is the sole input parameter to this function. It is typically used as a starting point for initial run-time memory allocations of thread stacks, queues, and memory pools.

> **Note:** *After initialization is complete, only an executing thread can create and delete system resources— including other threads. Therefore, at least one thread must be created during initialization.*

### Interrupts

Interrupts are left disabled during the entire initialization process. If the application somehow enables interrupts, unpredictable behavior may occur. Figure 4 shows the entire
initialization process, from system reset through application-specific initialization.
