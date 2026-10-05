---
id: "stream-readme-cmsisstream-shared-overhead"
type: "concept"
domain: "cmsis-stream"
title: "README: CMSISSTREAM_SHARED_OVERHEAD"
summary: "Additional memory required by std::allocate_shared."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:platform/cmsis_rtos_runtime/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/platform/cmsis_rtos_runtime/README.md#cmsisstream-shared-overhead"
license: "Apache-2.0"
mode: "V"
---

Additional memory required by `std::allocate_shared`.

When allocating a object of type `T` with `std::allocate_shared<T>` we need
enough memory for T and some additional memory required by the 
implementation of `std::shared_ptr`.
This parameter defines the additional memory required.
This value is used by the memory pool allocators to allocate enough memory.
The request to the allocator does not have the size `sizeof(T) + sizeof(std::shared_ptr<T>)`
It is slightly bigger.

Default value:
```C
#define CMSISSTREAM_SHARED_OVERHEAD 16
```
