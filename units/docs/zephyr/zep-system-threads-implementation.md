---
id: "zep-system-threads-implementation"
type: "concept"
domain: "rtos"
title: "System Threads: Implementation"
summary: "An application-supplied main() function begins executing once kernel initialization is complete. The kernel does not pass any arguments to the function, unless CONFIG_BOOTARGS is selected."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/system_threads.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/system_threads.rst"
license: "Apache-2.0"
mode: "V"
---

### Writing a main() function


An application-supplied `main()` function begins executing once
kernel initialization is complete. The kernel does not pass any arguments
to the function, unless `CONFIG_BOOTARGS` is selected. In such case the
kernel passes arguments to it and `main(int, char **)` can be used.

The following code outlines a trivial `main(void)` function.
The function used by a real application can be as complex as needed.

```c

int main(void)
{
    /* initialize a semaphore */
...

/* register an ISR that gives the semaphore */
...

/* monitor the semaphore forever */
while (1) {
    /* wait for the semaphore to be given by the ISR */
    ...
    /* do whatever processing is now needed */
    ...
}
}
```
