---
id: "threadx-chapter-2-installation-and-use-of-small-example-system"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of ThreadX: Small Example System"
summary: "The small example system in Figure 1 shows the creation of a single thread with a priority of 3. The thread executes, increments a counter, then sleeps for one clock tick. This process continues forever."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter2.md#small-example-system"
license: "MIT"
mode: "V"
---

The small example system in Figure 1 shows the creation of a single thread with a priority of 3. The thread executes, increments a counter, then sleeps for one clock tick.
This process continues forever.

```c
#include "tx_api.h"
unsigned long my_thread_counter = 0;
TX_THREAD my_thread;
main( )
{
    /* Enter the ThreadX kernel. */
    tx_kernel_enter( );
}
void tx_application_define(void *first_unused_memory)
{
    /* Create my_thread! */
    tx_thread_create(&my_thread, "My Thread",
    my_thread_entry, 0x1234, first_unused_memory, 1024,
    3, 3, TX_NO_TIME_SLICE, TX_AUTO_START);
}
void my_thread_entry(ULONG thread_input)
{
    /* Enter into a forever loop. */
    while(1)
    {
        /* Increment thread counter. */
        my_thread_counter++;
        /* Sleep for 1 tick. */
        tx_thread_sleep(1);
    }
}
```

**FIGURE 1. Template for Application Development**

Although this is a simple example, it provides a good template for real application development.
