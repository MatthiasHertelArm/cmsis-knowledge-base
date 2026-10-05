---
id: "txmw-chapter-2-usbx-host-stack-installa-initialization-of-usbx-resources"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Host Stack Installation: Initialization of USBX resources"
summary: "USBX has its own memory manager. The memory needs to be allocated to USBX before the host or device side of USBX is initialized. USBX memory manager can accommodate systems where memory can be cached."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-2.md#initialization-of-usbx-resources"
license: "MIT"
mode: "V"
---

USBX has its own memory manager. The memory needs to be allocated to USBX before the host or device side of USBX is initialized. USBX memory manager can accommodate systems where memory can be cached.

The following function initializes USBX memory resources with 128K of regular memory and no separate pool for cache safe memory:

```c
/* Initialize USBX Memory */

ux_system_initialize(memory_pointer,(128*1024),UX_NULL,0);
```

The prototype for the ux_system_initialize is as follows.

```c
UINT ux_system_initialize( 
    VOID *regular_memory_pool_start,
    ULONG regular_memory_size,
    VOID *cache_safe_memory_pool_start,
    ULONG cache_safe_memory_size);
```

### Input parameters:

- **regular_memory_pool_start** Beginning of the regular memory pool.
- **regular_memory_size** Size of the regular memory pool.
- **cache_safe_memory_pool_start** Beginning of the cache safe memory pool.
- **cache_safe_memory_size** Size of the cache safe memory pool.    |

Not all systems require the definition of cache safe memory. In such a system, the values passed during the initialization for the memory pointer will be set to UX_NULL and the size of the pool to 0. USBX will then use the regular memory pool in lieu of the cache safe pool.

In a system where the regular memory is not cache safe and a controller requires to perform DMA memory (like OHCI, EHCI controllers amongst others) it is necessary to define a memory pool in a cache safe zone.
