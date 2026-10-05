---
id: "txmw-chapter-3-module-manager-requireme-module-manager-sources"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Module Manager requirements: Module Manager sources"
summary: "The ThreadX Module Manager has a set of source files that are designed to be linked and located directly with the resident ThreadX code."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter3.md#module-manager-sources"
license: "MIT"
mode: "V"
---

The ThreadX Module Manager has a set of source files that are designed to be linked and located directly with the resident ThreadX code. These files provide the ability to launch a module and field subsequent ThreadX API requests from the module. The module manager files are as follows.

| **File Name** |  **Contents** |
|-------------- | ------------- |
| ***txm_module.h*** | Include file that defines module information (also included in the module source code). |
| ***txm_module_manager_dispatch.h*** | Include file that defines dispatch helper functions.|
| ***txm_module_manager_util.h*** | Include file that defines internal utility helper macros & functions. |
| ***txm_module_port.h*** | Include file that defines port-specific module information (also included in the module source code). |
| ***tx_initialize_low_level.\[s,S,68\]*** | Replaces existing ThreadX library file. Updated vector table and additional vector handlers for module manager and memory exceptions. *This file is only in Cortex-A7/ARM, Cortex-M7/ARM, Cortex-R4/ARM, Cortex-R4/IAR, MCF544xx/GHS, RX63/IAR, RX65N/IAR.*|
| ***tx_thread_context_restore.s*** | Replaces existing ThreadX library file. Restore thread context after interrupt processing. *This file is only in Cortex-A7/ARM, Cortex-R4/ARM, Cortex-R4/IAR.*|
| ***tx_thread_schedule.\[s,S,68\]*** | Replaces existing ThreadX library file. Extended scheduler code, which in this case is used to update memory management registers. |
| ***tx_thread_stack_build.s*** | Replaces existing ThreadX library file. Builds the stack frame of a thread. *This file is only in Cortex-A7/ARM, Cortex-R4/ARM, Cortex-R4/IAR.*|
| ***txm_module_manager_thread_stack_build.\[s,S,68\]*** | Builds all module initial stacks, includes setup for position-independent data access. |
| ***txm_module_manager_user_mode_entry.\[s,S\]*** | Allows the module to enter kernel mode. *This file is only in Cortex-A7/ARM, Cortex-R4/ARM, Cortex-R4/IAR.*|
| ***txm_module_manager_alignment_adjust.c*** | Handles port-specific alignment requirements.|
| ***txm_module_manager_application_request.c*** | Handles the application-specific requests to the resident code. |
| ***txm_module_manager_callback_request.c*** | Sends a callback request to a module. |
| ***txm_module_manager_event_flags_notify_trampoline.c*** | Processes the event flags set notification call from ThreadX. |
| ***txm_module_manager_external_memory_enable.c*** | Creates an entry in the memory management table for a shared memory space the module can access. |
| ***txm_module_manager_file_load.c*** | Allocates and loads a binary module file into the module memory area and prepares it for execution. |
| ***txm_module_manager_in_place_load.c*** | Allocates the module data area and prepares for module execution from the supplied code address. |
| ***txm_module_manager_initialize.c*** | Initializes the Module Manager, including specification of the module memory area available for loading and running modules. |
| ***txm_module_manager_initialize_mmu.c*** | Initialize MMU. Users can edit this file according to their memory map. *This file is only in Cortex-A7/ARM* |
| ***txm_module_manager_mm_initialize.c*** | Initialize MPU/MMU. Users can edit this file according to their memory map. *This file is only in Cortex-A7/ARM* |
| ***txm_module_manager_kernel_dispatch.c*** | Handles the module API requests, based on the request ID. |
| ***txm_module_manager_maximum_module_priority_set.c*** | Sets the maximum thread priority allowed in a module. |
| ***txm_module_manager_memory_fault_handler.c*** | Handles memory faults detected in an executing module. |
| ***txm_module_manager_memory_fault_notify.c*** | Registers an application notification callback whenever a memory fault occurs. |
| ***txm_module_manager_memory_load.c*** | Allocates and loads a module's code and data and prepares the module for execution. |
| ***txm_module_manager_mm_register_setup.c*** | Sets up MPU/MMU registers for the module based on where the code and data are loaded. |
| ***txm_module_manager_object_allocate.c*** | Allocates memory for a module object. |
| ***txm_module_manager_object_deallocate.c*** | Deallocates memory for a module object. |
| ***txm_module_manager_object_pointer_get.c*** | Searches for the supplied object type and name, and if found, returns the object pointer. |
| ***txm_module_manager_object_pointer_get_extended.c*** | Searches for the supplied object type and name, and if found, returns the object pointer. Name length specified for safety. |
| ***txm_module_manager_object_pool_create.c***  | Creates a pool of objects outside the module's data area that module applications can allocate from. |
| ***txm_module_manager_properties_get.c*** | Gets the properties of the specified module. |
| ***txm_module_manager_queue_notify_trampoline.c*** | Processes the queue notification call from ThreadX. |
| ***txm_module_manager_semaphore_notify_trampoline.c*** | Processes the semaphore put notification call from ThreadX.|
| ***txm_module_manager_start.c*** | Starts execution of a module. |
| ***txm_module_manager_stop.c*** | Stops execution of a module. |
| ***txm_module_manager_thread_create.c*** | Creates all module threads. |
| ***txm_module_manager_thread_notify_trampoline.c*** | Processes the thread entry/exit notification call from ThreadX. |
| ***txm_module_manager_thread_reset.c*** | Reset a module thread. |
| ***txm_module_manager_timer_notify_trampoline.c*** | Processes timer expirations from ThreadX. |
| ***txm_module_manager_unload.c*** | Unloads the module from the module memory area. |
| ***txm_module_manager_util.c*** | Internal helper functions for manager. |
