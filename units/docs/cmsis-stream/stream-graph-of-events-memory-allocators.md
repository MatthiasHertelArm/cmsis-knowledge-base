---
id: "stream-graph-of-events-memory-allocators"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Memory allocators"
summary: "It is possible to customize memory allocators to ensure that no uncontrolled memory allocation is occuring."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#memory-allocators"
license: "Apache-2.0"
mode: "V"
---

It is possible to customize memory allocators to ensure that no uncontrolled memory allocation is occuring.

Memory allocations are occuring in 4 cases:

- Allocation of a list of values (when several arguments are used for an event)
- Description for raw buffers and tensors
- Mutexes
- Content of raw buffer, tensor or std::string

### List of values

The maximum number of elements in a list is defined by the macro `CG_MAX_VALUES` that can be redefined. Its default value is 8. 

A `ListValue` always contains `CG_MAX_VALUES` `cg_value`. Its size if always the same even if less than `CG_MAX_VALUES` values are used.

Memory allocation of list is controlled with `CG_MK_LIST_EVENT_ALLOCATOR`.

A memory pool could be used since the size of `ListValue` is fixed.


Possible definitions:

- Default : `std::allocator<T> {}`
- Memory pool with C++ : `#define CG_MK_LIST_EVENT_ALLOCATOR(T) (std::pmr::polymorphic_allocator<T>(&pool))
`

where `pool` must be defined in one of the `.cpp` files and could be : 

`std::pmr::synchronized_pool_resource pool;`

- CMSIS-RTOS2 : `#define CG_MK_LIST_EVENT_ALLOCATOR(T) (CMSISEventPoolAllocator<T>{})`

where `CMSISEventPoolAllocator` is a __stateless__ memory allocator using a CMSIS RTOS memory pool.

See the implementation of `CMSISEventPoolAllocator` below in this document.

With CMSIS RTOS2, the memory pool can be created with:

```C++
cg_eventPool = osMemoryPoolNew(NB_MAX_EVENTS, sizeof(ListValue) + 16, NULL);
```

It is bigger than `ListValue` because the allocation is using a `std::shared_ptr` and the allocator is also allocating the control block for the `std::shared_ptr`.

It is difficult to know in a portable way what is the size of this control block. The easiest is to add a print in the custom memory allocator to measure the size of an allocation and use this size for the blocks of the memory pool.

On a Cortex-M55, it was measured to be `16` bytes so the memory pool block size is `sizeof(ListValue) + 16`.

### Description for buffers and tensors

Buffer and tensors are using a `ProtectedBuffer`. This protected buffer is allocating a `std::shared_ptr` to the underlying object descriptor.

The underlying object is describing the dimensions of the buffer and tensors and contains a pointer to the data. It does not contain the data. As consequence, the size of this descriptor is known and fixed.

`Tensor` is bigger than `Buffer` and should be used to dimension the blocks of the memory pool if a memory pool is used.

The macro used is `CG_MK_PROTECTED_BUF_ALLOCATOR` and it can be used like in the previous example.

In case of a stateless memory allocator, a different class must be used. `CMSISEventPoolAllocator` cannot be reused since a different memory pool with a different block size must be used.

### Mutexes

`ProtectedBuffer` are allocating a `std::shared_ptr` to a mutex. It is used to ensure that the `std::shared_ptr` to the data is protected (including the ref count).

Those memory blocks are much smaller and use a different memory allocator : `CG_MK_PROTECTED_MUTEX_ALLOCATOR`.

### Content of buffer, tensor and strings

Contrary to the prevous datastructure where the size of the data is always the same, the content of buffers is variable.

The content of data can be allocated on a object per object basis.

`std::string` can be created using an allocator and different `std::string` may use a different allocator.

Buffer and tensors use a `UniquePtr` that has unique ownership of the pointed data. The `UniquePtr` can be created with a stateless deleter and so can use any allocation strategy that make sense for the content.

By default, a `UniquePtr` created with a number of bytes or a `T*` will use the normal `std::free`.

If a `const T*` is used, no deleter is used by default.

### Memory allocation conclusion

With the use of the three custom memory allocators, it is possible to only use memory pools for the event system : so no fragmentation and deterministic allocations.

For the buffer / tensor content it depends on your application and how those objects are created.
