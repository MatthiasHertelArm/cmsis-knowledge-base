---
id: "threadx-chapter-4-description-of-threadx-s-tx-byte-release"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_byte_release"
summary: "This service releases a previously allocated memory area back to its associated pool."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-byte-release"
license: "MIT"
mode: "V"
---

Release bytes back to memory pool

### Prototype

```c
UINT tx_byte_release(VOID *memory_ptr);
```

### Description

This service releases a previously allocated memory area back to its associated pool. If there are one or more threads suspended waiting for memory from this pool, each suspended thread is given memory and resumed until the memory is exhausted or until there are no more suspended threads. This process of allocating memory to suspended threads always begins with the first thread suspended.

> **Note:** *The application may want to clear the memory area before releasing it to prevent data leaks.*

> **Important:** *The application must prevent using the memory area after it is released.*

### Parameters

- *memory_ptr*: Pointer to the previously allocated memory area.

### Return Values

- **TX_SUCCESS** (0x00) Successful memory release.
- **TX_PTR_ERROR** (0x03) Invalid memory area pointer.
- **TX_CALLER_ERROR** (0x13) Invalid caller of this service.

### Allowed From

Initialization and threads

### Preemption Possible

Yes

### Example

```c
unsigned char *memory_ptr;
UINT status;

/* Release a memory back to my_pool. Assume that the memory
area was previously allocated from my_pool. */
status = tx_byte_release((VOID *) memory_ptr);

/* If status equals TX_SUCCESS, the memory pointed to by
memory_ptr has been returned to the pool. */
```

### See Also

- [Block Pool Services](#Block_Pool_Services)
