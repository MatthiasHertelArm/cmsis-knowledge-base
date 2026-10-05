---
id: "zep-threads-thread-custom-data"
type: "concept"
domain: "rtos"
title: "Threads: Thread Custom Data"
summary: "Every thread has a 32-bit custom data area, accessible only by the thread itself, and may be used by the application for any purpose it chooses. The default custom data value for a thread is zero."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

Every thread has a 32-bit `custom data` area, accessible only by
the thread itself, and may be used by the application for any purpose
it chooses. The default custom data value for a thread is zero.


**Note:** Custom data support is not available to ISRs because they operate within a single shared kernel interrupt handling context.

By default, thread custom data support is disabled. The configuration option
`CONFIG_THREAD_CUSTOM_DATA` can be used to enable support.

The `k_thread_custom_data_set` and
`k_thread_custom_data_get` functions are used to write and read
a thread's custom data, respectively. A thread can only access its own
custom data, and not that of another thread.

The following code uses the custom data feature to record the number of times
each thread calls a specific routine.


**Note:** Obviously, only a single routine can use this technique, since it monopolizes the use of the custom data feature.

```c

int call_tracking_routine(void)
{
    uint32_t call_count;

    if (k_is_in_isr()) {
    /* ignore any call made by an ISR */
    } else {
        call_count = (uint32_t)k_thread_custom_data_get();
        call_count++;
        k_thread_custom_data_set((void *)call_count);
}

    /* do rest of routine's processing */
    ...
}
```
Use thread custom data to allow a routine to access thread-specific information,
by using the custom data as a pointer to a data structure owned by the thread.
