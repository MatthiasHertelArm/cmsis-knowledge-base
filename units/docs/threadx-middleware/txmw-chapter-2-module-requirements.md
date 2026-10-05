---
id: "txmw-chapter-2-module-requirements"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Module requirements"
summary: "A ThreadX Module contains a preamble, which defines the basic characteristics of the module. The preamble is followed by the instruction area of the module."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter2.md"
license: "MIT"
mode: "V"
---

A ThreadX Module contains a preamble, which defines the basic characteristics of the module. The preamble is followed by the instruction area of the module. Modules may be executed in place or they may be loaded into the module memory area by the Module Manager prior to execution. The only requirement is that the preamble is always located at the first address of the module. Figure 2 illustrates a basic module layout.

| Module Layout |
|:---:|
| \[module preamble\]         |
| \[module instruction area\] |
| \[module RAM area\]         |

**Figure 2** - Module Layout

> **Note:** Modules must be built with the appropriate position independent code and data compiler/linker options. This enables execution of the module in any memory area.

When a Module thread is created, a second stack space is allocated for use when the thread is in the memory-protected kernel. The size of the thread's kernel stack space is user-configurable using **TXM_MODULE_KERNEL_STACK_SIZE** in ***txm_module_port.h***. This allows a smaller stack size to be used when creating a Module thread, as the stack specified by the user when calling ***tx_thread_create*** is only used in the module.

> **Note:** The top of a module thread stack contains the thread entry information structure (**TXM_MODULE_THREAD_ENTRY_INFO**), so the available stack size is decreased by the size of this structure. When creating a thread in a module, increase its stack size by at least this the size of this structure.

The following steps are required for creating and building a ThreadX Module (each step is described in greater detail below).

1. All C files in a module must #define **TXM_MODULE** prior to including ***txm_module.h***. This can be accomplished in the source file being compiled or as part of the project settings. Doing so remaps the ThreadX API calls to the module-specific version of the API that invokes the dispatch function in the resident Module Manager to perform the call to the actual API function.
2. Each module must have a preamble at its first instruction area address which defines the characteristics and the resource needs of the module.
3. Each module must link the preamble at the beginning of the module instruction area.
4. Each module must link against a module library (***txm.a***), which contains module-specific functions used to interact with ThreadX.
