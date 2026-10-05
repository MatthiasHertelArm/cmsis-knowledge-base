---
id: "txmw-chapter-3-module-manager-requireme"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Module Manager requirements"
summary: "The ThreadX Module Manager resides in the resident portion of the application along with the ThreadX RTOS. It is responsible for starting the module as well as fielding and dispatching all module requests for ThreadX API services."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter3.md"
license: "MIT"
mode: "V"
---

The ThreadX Module Manager resides in the resident portion of the application along with the ThreadX RTOS. It is responsible for starting the module as well as fielding and dispatching all module requests for ThreadX API services.

> **Note:** The ThreadX Module **Manager** source files (C and assembly) should be added to the ThreadX library project "**tx**".

The following steps are required for building the ThreadX Module Manager (each step is described in greater detail below).

1. The **TX_THREAD** control block must be extended to include module information. The easiest way to accomplish this is to replace the definition of **TX_THREAD_EXTENSION_2** in the ***tx_port.h*** file with the **TX_THREAD_EXTENSION_2** found in ***txm_module_port.h***. See [appendix](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/appendix.md) for port-specific extensions.

   Example extension:

   ```c
   #define TX_THREAD_EXTENSION_2                     \
       VOID      tx_thread_module_instance_ptr;      \
       VOID      tx_thread_module_entry_info_ptr;    \
       ULONG     tx_thread_module_current_user_mode; \
       ULONG     tx_thread_module_user_mode;         \
       VOID     *tx_thread_module_kernel_stack_start;\
       VOID     *tx_thread_module_kernel_stack_end;  \
       ULONG     tx_thread_module_kernel_stack_size; \
       VOID     *tx_thread_module_stack_ptr;         \
       VOID     *tx_thread_module_stack_start;       \
       VOID     *tx_thread_module_stack_end;         \
       ULONG     tx_thread_module_stack_size;        \
       VOID     *tx_thread_module_reserved;
   ```

   The following extensions must be defined in ***tx_port.h***.

   ```c
   #define TX_EVENT_FLAGS_GROUP_EXTENSION  VOID    *tx_event_flags_group_module_instance; \
        VOID   (*tx_event_flags_group_set_module_notify)(struct TX_EVENT_FLAGS_GROUP_STRUCT *group_ptr);
   
   #define TX_QUEUE_EXTENSION              VOID    *tx_queue_module_instance; \
        VOID   (*tx_queue_send_module_notify)(struct TX_QUEUE_STRUCT *queue_ptr);
   
   #define TX_SEMAPHORE_EXTENSION          VOID    *tx_semaphore_module_instance; \
        VOID   (*tx_semaphore_put_module_notify)(struct TX_SEMAPHORE_STRUCT *semaphore_ptr);
   
   #define TX_TIMER_EXTENSION              VOID    *tx_timer_module_instance; \
        VOID   (*tx_timer_module_expiration_function)(ULONG id);
   ```

2. Add all the ***txm_module_manager_\**** C and assembly files to the ThreadX library project ***tx***.
3. Rebuild all libraries and executable projects. If NetX Duo is required, all Module and Module Manager C code should be built with **TXM_MODULE_ENABLE_NETX_DUO** defined.
