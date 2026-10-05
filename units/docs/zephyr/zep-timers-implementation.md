---
id: "zep-timers-implementation"
type: "concept"
domain: "rtos"
title: "Timers: Implementation"
summary: "A timer is defined using a variable of type k_timer. It must then be initialized by calling k_timer_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/timing/timers.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/timing/timers.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a Timer


A timer is defined using a variable of type `k_timer`.
It must then be initialized by calling `k_timer_init`.

The following code defines and initializes a timer.

```c

struct k_timer my_timer;
extern void my_expiry_function(struct k_timer *timer_id);

k_timer_init(&my_timer, my_expiry_function, NULL);
```
Alternatively, a timer can be defined and initialized at compile time
by calling `K_TIMER_DEFINE`.

The following code has the same effect as the code segment above.

```c

K_TIMER_DEFINE(my_timer, my_expiry_function, NULL);
```

### Using a Timer Expiry Function


The following code uses a timer to perform a non-trivial action on a periodic
basis. Since the required work cannot be done at the interrupt level,
the timer's expiry function submits a work item to the
system workqueue, whose thread performs the work.

```c

void my_work_handler(struct k_work *work)
{
    /* do the processing that needs to be done periodically */
    ...
}

K_WORK_DEFINE(my_work, my_work_handler);

void my_timer_handler(struct k_timer *dummy)
{
    k_work_submit(&my_work);
}

K_TIMER_DEFINE(my_timer, my_timer_handler, NULL);

...

/* start a periodic timer that expires once every second */
k_timer_start(&my_timer, K_SECONDS(1), K_SECONDS(1));
```

### Reading Timer Status


The following code reads a timer's status directly to determine
if the timer has expired or not.

```c

K_TIMER_DEFINE(my_status_timer, NULL, NULL);

...

/* start a one-shot timer that expires after 200 ms */
k_timer_start(&my_status_timer, K_MSEC(200), K_NO_WAIT);

/* do work */
...

/* check timer status */
if (k_timer_status_get(&my_status_timer) > 0) {
    /* timer has expired */
} else if (k_timer_remaining_get(&my_status_timer) == 0) {
    /* timer was stopped (by someone else) before expiring */
} else {
    /* timer is still running */
}
```

### Using Timer Status Synchronization


The following code performs timer status synchronization to allow a thread
to do useful work while ensuring that a pair of protocol operations
are separated by the specified time interval.

```c

K_TIMER_DEFINE(my_sync_timer, NULL, NULL);

...

/* do first protocol operation */
...

/* start a one-shot timer that expires after 500 ms */
k_timer_start(&my_sync_timer, K_MSEC(500), K_NO_WAIT);

/* do other work */
...

/* ensure timer has expired (waiting for expiry, if necessary) */
k_timer_status_sync(&my_sync_timer);

/* do second protocol operation */
...
```

**Note:** If the thread had no other work to do it could simply sleep between the two protocol operations, without using a timer.
