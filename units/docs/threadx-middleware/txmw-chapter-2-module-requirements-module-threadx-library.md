---
id: "txmw-chapter-2-module-requirements-module-threadx-library"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Module requirements: Module ThreadX library"
summary: "Each module must link against a special, module-centric ThreadX library. This library provides access to ThreadX services in the resident code. Most of the access is accomplished via the txm\\.c files."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter2.md#module-threadx-library"
license: "MIT"
mode: "V"
---

Each module must link against a special, module-centric ThreadX library. This library provides access to ThreadX services in the resident code. Most of the access is accomplished via the ***txm_\*.c*** files. The following is an example of the module access call for the ThreadX API function ***tx_thread_relinquish*** (in ***\*txm_thread_relinquish.c\****).

```c
(_txm_module_kernel_call_dispatcher)(TXM_THREAD_RELINQUISH_CALL, 0, 0, 0);
```

In this example, the function pointer supplied by the Module Manager is used to call the Module Manager dispatch function with the ID associated with the ***tx_thread_relinquish*** service. This service takes no parameters.
