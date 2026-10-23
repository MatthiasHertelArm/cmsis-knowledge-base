---
id: "zep-threads-implementation"
type: "concept"
domain: "rtos"
title: "Threads: Implementation"
summary: "A thread is spawned by defining its stack area and its thread control block, and then calling k_thread_create."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

### Spawning a Thread


A thread is spawned by defining its stack area and its thread control block,
and then calling `k_thread_create`.

The stack area may be statically allocated using
`K_THREAD_STACK_DEFINE` or `K_KERNEL_STACK_DEFINE` to ensure
it is properly set up in memory.

The size parameter for the stack must be one of three values:

- The original requested stack size passed to
  `K_THREAD_STACK` or `K_KERNEL_STACK` family of stack instantiation
  macros.
- For a stack object defined with the `K_THREAD_STACK` family of
  macros, the return value of `K_THREAD_STACK_SIZEOF()` for that
  object.
- For a stack object defined with the `K_KERNEL_STACK` family of
  macros, the return value of `K_KERNEL_STACK_SIZEOF()` for that
  object.

Alternatively, the stack area may be dynamically allocated using
`k_thread_stack_alloc` and freed using `k_thread_stack_free`.

The thread spawning function returns its thread id, which can be used
to reference the thread.

The following code spawns a thread that starts immediately.

```c

#define MY_STACK_SIZE 500
#define MY_PRIORITY 5

extern void my_entry_point(void *, void *, void *);

K_THREAD_STACK_DEFINE(my_stack_area, MY_STACK_SIZE);
struct k_thread my_thread_data;

k_tid_t my_tid = k_thread_create(&my_thread_data, my_stack_area,
                                 K_THREAD_STACK_SIZEOF(my_stack_area),
                                 my_entry_point,
                                 NULL, NULL, NULL,
                                 MY_PRIORITY, 0, K_NO_WAIT);
```
Alternatively, a thread can be declared at compile time by calling
`K_THREAD_DEFINE`. Observe that the macro defines
the stack area, control block, and thread id variables automatically.

The following code has the same effect as the code segment above.

```c

#define MY_STACK_SIZE 500
#define MY_PRIORITY 5

extern void my_entry_point(void *, void *, void *);

K_THREAD_DEFINE(my_tid, MY_STACK_SIZE,
                my_entry_point, NULL, NULL, NULL,
                MY_PRIORITY, 0, 0);
```

**Note:** The delay parameter to `k_thread_create` is a thread immediately. The corresponding parameter to `K_THREAD_DEFINE` is a duration in integral milliseconds, so the equivalent argument is 0.

The following code dynamically allocates a thread stack, waits until the thread
has joined, and then frees the dynamically allocated thread stack.

```c

extern void my_entry_point(void *, void *, void *);

k_tid_t my_tid;
void *my_stack_area;

my_stack_area = k_thread_stack_alloc(CONFIG_DYNAMIC_THREAD_STACK_SIZE);
my_tid = k_thread_create(&my_thread_data, my_stack_area,
                          CONFIG_DYNAMIC_THREAD_STACK_SIZE,
                          my_entry_point,
                          NULL, NULL, NULL,
                          MY_PRIORITY, 0, K_NO_WAIT);
k_thread_join(my_tid, K_FOREVER);
k_thread_stack_free(my_stack_area);
```

#### User Mode Constraints


This section only applies if `CONFIG_USERSPACE` is enabled, and a user
thread tries to create a new thread. The `k_thread_create` API is
still used, but there are additional constraints which must be met or the
calling thread will be terminated:

* The calling thread must have permissions granted on both the child thread
  and stack parameters; both are tracked by the kernel as kernel objects.

* The child thread and stack objects must be in an uninitialized state,
  i.e. it is not currently running and the stack memory is unused.

* The stack size parameter passed in must be equal to or less than the
  bounds of the stack object when it was declared.

* The `K_USER` option must be used, as user threads can only create
  other user threads.

* The `K_ESSENTIAL` option must not be used, user threads may not be
  considered essential threads.

* The priority of the child thread must be a valid priority value, and equal to
  or lower than the parent thread.


### Dropping Permissions


If `CONFIG_USERSPACE` is enabled, a thread running in supervisor mode
may perform a one-way transition to user mode using the
`k_thread_user_mode_enter` API. This is a one-way operation which
will reset and zero the thread's stack memory. The thread will be marked
as non-essential.


### Terminating a Thread


A thread terminates itself by returning from its entry point function.

The following code illustrates the ways a thread can terminate.

```c

void my_entry_point(int unused1, int unused2, int unused3)
{
    while (1) {
        ...
    if (<some condition>) {
        return; /* thread terminates from mid-entry point function */
    }
    ...
    }

    /* thread terminates at end of entry point function */
}
```
If `CONFIG_USERSPACE` is enabled, aborting a thread will additionally
mark the thread and stack objects as uninitialized so that they may be reused.
