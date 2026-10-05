---
id: "zep-scheduling-suggested-uses-2"
type: "concept"
domain: "rtos"
title: "Scheduling: Suggested Uses"
summary: "Use k_cpu_atomic_idle when a thread has to do some real work in addition to idling the CPU to wait for an event. See example above."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

Use `k_cpu_atomic_idle` when a thread has to do some real work in addition to
idling the CPU to wait for an event. See example above.

Use `k_cpu_idle` only when a thread is only responsible for idling the CPU,
i.e. not doing any real work, like in this example below.

```c

int main(void)
{
    /* ... do some system/application initialization */


    /* thread is only used for CPU idling from this point on */
    for (;;) {
        k_cpu_idle();
    }
}
```

**Note:** **Do not use these APIs unless absolutely necessary.** In a normal system, the idle thread takes care of power management, including CPU idling.
