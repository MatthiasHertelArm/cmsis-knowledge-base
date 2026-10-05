---
id: "intr-practical-design-patterns-opaque-p-what-if-i-don-t-want-to-dynamically-allo"
type: "concept"
domain: "debug"
title: "Practical Design Patterns: Opaque Pointers and Objects in C: What If I Don't Want to Dynamically Allocate Memory?"
summary: "There are some reading this that have their spidey sense tingling when they see the word calloc in ringbuffer_create."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-11-opaque-pointers.md"
doc_source: "https://interrupt.memfault.com/blog/opaque-pointers#what-if-i-don-t-want-to-dynamically-allocate-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are some reading this that have their spidey sense tingling when
they see the word `calloc` in `ringbuffer_create`.

In many embedded systems, dynamic memory allocation is strongly discouraged
or outright forbidden. Even if it's not forbidden,
it's often a good idea to eliminate dynamic memory if static memory suffices.

In the example, we could statically allocate an array of some maximum number of ringbuffers,
and give the user a `uint32_t` handle, which is an index into the array.

The example code would look slightly different:

`ringbuffer.h`

```c
// ...
typedef uint32_t ringbuffer_t;
// ...
```

`ringbuffer.c`

```c
#include "ringbuffer.h"

#define MAX_NUM_RINGBUFFERS 10
#define MAX_RINGBUFFER_CAPACITY 100

struct ringbuffer_instance_t {
    volatile uint32_t wr_pos;
    volatile uint32_t rd_pos;
    uint8_t data[MAX_RINGBUFFER_CAPACITY];
    uint32_t capacity;
};

static struct ringbuffer_instance_t g_instances[MAX_NUM_RINGBUFFERS];
static bool g_instance_in_use[MAX_NUM_RINGBUFFERS];

ringbuffer_t ringbuffer_create(uint32_t capacity) {
    // Search for an instance that is not in use
    for (uint32_t i = 0; i < MAX_NUM_RINGBUFFERS; i++) {
        if (!g_instance_in_use[i]) {
            g_instance_in_use[i] = true;
            g_instances[i].wr_pos = 0;
            g_instances[i].rd_pos = 0;
            g_instances[i].capacity = capacity;
            return i;
        }
    }

    // No available instances, fail hard here.
    // Alternatively, could return an error code and let the user handle it.
    assert(false);
}

uint32_t ringbuffer_capacity(ringbuffer_t handle) {
    return g_instances[handle].capacity;
}

// ...

void ringbuffer_destroy(ringbuffer_t handle) {
    g_instance_in_use[handle] = false;
}
```

Notice that it's still possible to run out of instances, which is similar to a dynamic
memory allocation failure. The benefit of static memory is that problems like
fragmentation are avoided.
Ultimately, the system designer still needs to think about how to handle failed
instance creation.

One downside to this approach is that it can be wasteful of memory. If you create an
array that is capable of holding 100 instances, and you only ever create one instance,
then you've wasted the memory of 99 instances. Furthermore, for a specific instance, if the
user only needs a capacity of 25, then the other 75 slots are completely unused.

Some might balk at the performance of the linear scan in `ringbuffer_create`.
In practice, I've found it's rarely a concern, especially if you have a small number of instances
(ten or less), or if you rarely call `*_create` (e.g. only once at system startup).

The linear scan could become a concern if you create and destroy instances many times (e.g. inside
of a loop), or if you have a large number of instances, in which case you probably
don't want to pay the `O(n)` price each time. For those cases, a linked list
of available instances is a good approach.

My personal approach - dynamic memory is okay if it's only allocated at system startup,
and not during normal operation.
The implementation is much simpler using dynamic memory.
