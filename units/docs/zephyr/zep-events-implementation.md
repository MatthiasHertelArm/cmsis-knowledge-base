---
id: "zep-events-implementation"
type: "concept"
domain: "rtos"
title: "Events: Implementation"
summary: "An event object is defined using a variable of type k_event. It must then be initialized by calling k_event_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/events.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/events.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining an Event Object


An event object is defined using a variable of type `k_event`.
It must then be initialized by calling `k_event_init`.

The following code defines an event object.

```c

struct k_event my_event;

k_event_init(&my_event);
```
Alternatively, an event object can be defined and initialized at compile time
by calling `K_EVENT_DEFINE`.

The following code has the same effect as the code segment above.

```c

K_EVENT_DEFINE(my_event);
```

### Setting Events


Events in an event object are set by calling `k_event_set`.

The following code builds on the example above, and sets the events tracked by
the event object to 0x001.

```c

void input_available_interrupt_handler(void *arg)
{
    /* notify threads that data is available */

    k_event_set(&my_event, 0x001);

    ...
}
```

### Posting Events


Events are posted to an event object by calling `k_event_post`.

The following code builds on the example above, and posts a set of events to
the event object.

```c

void input_available_interrupt_handler(void *arg)
{
    ...

    /* notify threads that more data is available */

    k_event_post(&my_event, 0x120);

    ...
}
```

### Waiting for Events (without removal)


Threads wait for events by calling `k_event_wait`.

The following code builds on the example above, and waits up to 50 milliseconds
for any of the specified events to be posted.  A warning is issued if none
of the events are posted in time.

```c

void consumer_thread(void)
{
    uint32_t  events;

    events = k_event_wait(&my_event, 0xFFF, false, K_MSEC(50));
    if (events == 0) {
        printk("No input devices are available!");
    } else {
        /* Access the desired input device(s) */
        ...
    }
    ...
}
```
Alternatively, the consumer thread may desire to wait for all the events
before continuing using `k_event_wait_all`.

```c

void consumer_thread(void)
{
    uint32_t  events;

    events = k_event_wait_all(&my_event, 0x121, false, K_MSEC(50));
    if (events == 0) {
        printk("At least one input device is not available!");
    } else {
        /* Access the desired input devices */
        ...
    }
    ...
}
```

### Waiting for Events (with removal)


Threads wait for events (with atomic removal upon receipt) by calling
`k_event_wait_safe`.

The following code builds on the example above, and waits up to 50 milliseconds
for any of the specified events to be posted.  A warning is issued if none
of the events are posted in time.

If events are received on time, then they will not be present in the event
object until the next time that the events are set or posted.

```c

void consumer_thread(void)
{
    uint32_t  events;

    events = k_event_wait_safe(&my_event, 0xFFF, false, K_MSEC(50));
    if (events == 0) {
        printk("No input devices are available!");
    } else {
        /* Access the desired input device(s) */
        ...
    }
    ...
}
```
Alternatively, the consumer thread may desire to wait for all the events
(with atomic removal upon receipt) before continuing using
`k_event_wait_all_safe`.

If all events are received on time, then they will not be present in the event
object until the next time that the events are set or posted.

```c

void consumer_thread(void)
{
    uint32_t  events;

    events = k_event_wait_all_safe(&my_event, 0x121, false, K_MSEC(50));
    if (events == 0) {
        printk("At least one input device is not available!");
    } else {
        /* Access the desired input devices */
        ...
    }
    ...
}
```
