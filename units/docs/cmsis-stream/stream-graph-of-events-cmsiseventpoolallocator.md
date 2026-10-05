---
id: "stream-graph-of-events-cmsiseventpoolallocator"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: CMSISEventPoolAllocator"
summary: "Here is an example of a C++ _stateless_ memory allocator using a CMSIS RTOS memory pool."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#cmsiseventpoolallocator"
license: "Apache-2.0"
mode: "V"
---

Here is an example of a C++ __stateless__ memory allocator using a CMSIS RTOS memory pool.

In case of a memory pool, we cannot allocate block of varying sizes.

As consequence, the `allocator` method has a test:
```C++
if ((n == 1) && (sizeof(T) <= osMemoryPoolGetBlockSize(cg_eventPool)))
```

`n` is the number of samples of type `T`. In our case, we always allocate either one `ListValue`, or one `TensorPtr<T>` or one mutex. So `n` should always be equal to 1.

Then, we should not request more than what can be contained in a block of the memory pool.

In practice, the condition should always be true because this memory allocator is not used to make more general memory allocations.


```C++
template <typename T>
class CMSISEventPoolAllocator
{
public:
    using value_type = T;
    using is_always_equal = std::true_type;

    CMSISEventPoolAllocator() noexcept = default;

    template <typename U>
    CMSISEventPoolAllocator(const CMSISEventPoolAllocator<U> &) noexcept {}

    template <typename U>
    struct rebind
    {
        using other = CMSISEventPoolAllocator<U>;
    };

    T *allocate(std::size_t n)
    {
        if ((n == 1) && (sizeof(T) <= osMemoryPoolGetBlockSize(cg_eventPool)))
        {
            //printf("Alloc event %d\n",sizeof(T));
            return static_cast<T *>(osMemoryPoolAlloc(cg_eventPool,0));
        }
        else
        {
           return nullptr;
        }
    };

    void deallocate(T *p, std::size_t n) noexcept
    {
        osMemoryPoolFree(cg_eventPool,static_cast<void*>(p));
    };

};

template <typename T, typename U>
bool operator==(const CMSISEventPoolAllocator<T> &, const CMSISEventPoolAllocator<U> &) { return true; }

template <typename T, typename U>
bool operator!=(const CMSISEventPoolAllocator<T> &, const CMSISEventPoolAllocator<U> &) { return false; }

```
