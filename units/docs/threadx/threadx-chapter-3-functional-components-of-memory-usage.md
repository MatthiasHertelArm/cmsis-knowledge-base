---
id: "threadx-chapter-3-functional-components-of-memory-usage"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Memory Usage"
summary: "ThreadX resides along with the application program. As a result, the static memory (or fixed memory) usage of ThreadX is determined by the development tools; e.g., the compiler, linker, and locator."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#memory-usage"
license: "MIT"
mode: "V"
---

ThreadX resides along with the application program. As a result, the static memory (or fixed memory) usage of ThreadX is determined by the development tools; e.g., the
compiler, linker, and locator. Dynamic memory (or run-time memory) usage is under direct control of the application.

### Static Memory Usage

Most of the development tools divide the application program image into five basic areas: *instruction*, *constant*, *initialized data*, *uninitialized data*, and *system
stack*. Figure 3 shows an example of these memory areas.

It is important to understand that this is only an example. The actual static memory layout is specific to the processor, development tools, and the underlying hardware.

The instruction area contains all of the program's processor instructions. This area is typically the largest and is often located in ROM.

The constant area contains various compiled constants, including strings defined or referenced within the program. In addition, this area contains the "initial copy" of the initialized data area. During the *Memory Usage* compiler's initialization process, this portion of the constant area is used to set up the initialized data area in RAM. The constant area usually follows the instruction area and is often located in ROM.

The initialized data and uninitialized data areas contain all of the global and static variables. These areas are always located in RAM.

The system stack is generally set up immediately following the initialized and uninitialized data areas.

The system stack is used by the compiler during initialization, then by ThreadX during initialization and, subsequently, in ISR processing.

(figure: Memory Area Example)

**FIGURE 3. Memory Area Example**

### Dynamic Memory Usage

As mentioned before, dynamic memory usage is under direct control of the application. Control blocks and memory areas associated with stacks, queues, and memory pools can be placed anywhere in the target's memory space. This is an important feature because it facilitates easy utilization of different types of physical memory.

For example, suppose a target hardware environment has both fast memory and slow memory. If the application needs extra performance for a high-priority thread, its control block
(TX_THREAD) and stack can be placed in the fast memory area, which may greatly enhance its performance.
