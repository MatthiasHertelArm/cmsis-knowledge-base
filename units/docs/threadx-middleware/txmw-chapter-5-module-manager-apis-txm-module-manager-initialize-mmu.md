---
id: "txmw-chapter-5-module-manager-apis-txm-module-manager-initialize-mmu"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Module Manager APIs: txm_module_manager_initialize_mmu"
summary: "Initialize the memory management hardware."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter5.md#txm-module-manager-initialize-mmu"
license: "MIT"
mode: "V"
---

Initialize the memory management hardware.

### Prototype

```c
UINT txm_module_manager_initialize_mmu(VOID);
```

### Description

This service initializes the MMU.

### Input parameters

none

### Return values

- **TX_SUCCESS** (0x00) Successful initialization.
- **TX_CALLER_ERROR** (0x13) Invalid caller.

### Allowed from

Initialization and Threads

### Example

```c
/* Initialize the module manager with 64KB of RAM starting at address 0x64010000. */
txm_module_manager_initialize((VOID *) 0x64010000, 0x10000);

/* Initialize the MMU. */
txm_module_manager_initialize_mmu();
```

---
