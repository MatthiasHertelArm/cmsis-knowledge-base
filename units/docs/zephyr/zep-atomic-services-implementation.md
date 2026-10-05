---
id: "zep-atomic-services-implementation"
type: "concept"
domain: "rtos"
title: "Atomic Services: Implementation"
summary: "An atomic variable is defined using a variable of type atomic_t."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/other/atomic.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/other/atomic.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining an Atomic Variable


An atomic variable is defined using a variable of type `atomic_t`.

By default an atomic variable is initialized to zero. However, it can be given
a different value using `ATOMIC_INIT`:

```c

atomic_t flags = ATOMIC_INIT(0xFF);
```

### Manipulating an Atomic Variable


An atomic variable is manipulated using the APIs listed at the end of
this section.

The following code shows how an atomic variable can be used to keep track
of the number of times a function has been invoked. Since the count is
incremented atomically, there is no risk that it will become corrupted
in mid-increment if a thread calling the function is interrupted if
by a higher priority context that also calls the routine.

```c

atomic_t call_count;

int call_counting_routine(void)
{
    /* increment invocation counter */
    atomic_inc(&call_count);

    /* do rest of routine's processing */
    ...
}
```

### Manipulating an Array of Atomic Variables


An array of 32-bit atomic variables can be defined in the conventional manner.
However, you can also define an N-bit array of atomic variables using
`ATOMIC_DEFINE`.

A single bit in array of atomic variables can be manipulated using
the APIs listed at the end of this section that end with `_bit`.

The following code shows how a set of 200 flag bits can be implemented
using an array of atomic variables.

```c

#define NUM_FLAG_BITS 200

ATOMIC_DEFINE(flag_bits, NUM_FLAG_BITS);

/* set specified flag bit & return its previous value */
int set_flag_bit(int bit_position)
{
    return (int)atomic_set_bit(flag_bits, bit_position);
}
```

### Memory Ordering


For consistency and correctness, all Zephyr atomic APIs are expected
to include a full memory barrier (in the sense of e.g. "serializing"
instructions on x86, "DMB" on ARM, or a "sequentially consistent"
operation as defined by the C++ memory model) where needed by hardware
to guarantee a reliable picture across contexts.  Any
architecture-specific implementations are responsible for ensuring
this behavior.
