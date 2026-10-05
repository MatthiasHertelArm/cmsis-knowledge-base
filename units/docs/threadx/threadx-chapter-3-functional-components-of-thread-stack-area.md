---
id: "threadx-chapter-3-functional-components-of-thread-stack-area"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX: Thread Execution / Thread Stack Area"
summary: "Each thread must have its own stack for saving the context of its last execution and compiler use. Most C compilers use the stack for making function calls and for temporarily allocating local variables."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter3.md#thread-stack-area"
license: "MIT"
mode: "V"
---

_Part of: Thread Execution_

Each thread must have its own stack for saving the context of its last execution and compiler use. Most C compilers use the stack for making function calls and for temporarily allocating local variables. Figure 6 shows a typical thread's stack.

Where a thread stack is located in memory is up to the application. The stack area is specified during thread creation and can be located anywhere in the target's address space. This is an important feature because it allows applications to improve performance of important threads by placing their stack in high-speed RAM.

**Stack Memory Area** (example)

(figure: Typical Thread Stack)

**FIGURE 6. Typical Thread Stack**

How big a stack should be is one of the most frequently asked questions about threads. A thread's stack area must be large enough to accommodate worst-case function call nesting, local variable allocation, and saving its last execution context.

The minimum stack size, **TX_MINIMUM_STACK**, is defined by ThreadX. A stack of this size supports saving a thread's context and minimum amount of function calls and local variable allocation.

For most threads, however, the minimum stack size is too small, and the user must ascertain the worst-case size requirement by examining function-call nesting and local variable allocation. Of course, it is always better to start with a larger stack area.

After the application is debugged, it is possible to tune the thread stack sizes if memory is scarce. A favorite trick is to preset all stack areas with an easily identifiable data pattern like (0xEFEF) prior to creating the threads. After the application has been thoroughly put through its paces, the stack areas can be examined to see how much stack was actually used by finding the area of the stack where the data pattern is still intact. Figure 7 shows a stack preset to 0xEFEF after thorough thread execution.

**Stack Memory Area** (another example)

(figure: Stack Preset to 0xEFEF*)

**FIGURE 7. Stack Preset to 0xEFEF**

> **Important:** *By default, ThreadX initializes every byte of each thread stack with a value of 0xEF.*
