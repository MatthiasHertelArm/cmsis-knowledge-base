---
id: "txmw-chapter-2-module-requirements-module-sources"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Module requirements: Module sources"
summary: "ThreadX Modules have their own set of source files that are designed to be linked and located directly with the module source code. These files provide the bridge between the separate module and resident Module Manager."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter2.md#module-sources"
license: "MIT"
mode: "V"
---

ThreadX Modules have their own set of source files that are designed to be linked and located directly with the module source code. These files provide the bridge between the separate module and resident Module Manager. The Module files are as follows.

| File Name | Contents |
|---|---|
| **txm_module.h** | Include file that defines module information. |
| **txm_module_port.h** | Include file that defines port-specific module information. |
| **txm_module_user.h** | Defines and values the user can customize. |
| **txm_module_initialize.s [1][3]** | Calls intrinsic functions to startup module. |
| **txm_module_preamble.\{s/S/68\}** | Module preamble assembly file. This file defines various module-specific attributes and is linked with the module application code. |
| **txm_module_application_request.c [1]** | Module application request function sends an application-specific request to the resident code. |
| **txm_module_callback_request_thread_entry.c [1]** | Module callback thread that is responsible for processing callbacks requested by the module, including timers and notification callbacks. |
| **txm_*.c [1][2]** | The standard ThreadX API services, these call the kernel dispatcher.
| **txm_module_object_allocate.c [1]** | Module function to allocate memory for module objects located in the manager memory pool. |
| **txm_module_object_deallocate.c [1]** | Module function to deallocate memory for module objects located in the manager memory pool. |
| **txm_module_object_pointer_get.c [1]** | Module function to retrieve a pointer to a system object. |
| **txm_module_object_pointer_get_extended.c [1]** | Module function to retrieve a pointer to a system object, name length safety. |
| **txm_module_thread_shell_entry.c [1]** | Module thread entry function. |
| **txm_module_thread_system_suspend.c [1]** | Module function to suspend a thread. |

**[1]** Located in library ***txm.a***.

**[2]** These files have the same name as the ThreadX API files, with **txm_** prefix instead of **tx_** prefix.

**[3]** The **txm_module_initialize.s** file is only for ports using ARM tools.
