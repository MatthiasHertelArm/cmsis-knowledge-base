---
id: "zep-polling-api-implementation"
type: "concept"
domain: "rtos"
title: "Polling API: Implementation"
summary: "The main API is k_poll, which operates on an array of poll events of type k_poll_event. Each entry in the array represents one event with a condition, which a call to k_poll will wait for to be fulfilled."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/polling.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/polling.rst"
license: "Apache-2.0"
mode: "V"
---

### Using k_poll()


The main API is `k_poll`, which operates on an array of poll events
of type `k_poll_event`. Each entry in the array represents one
event with a condition, which a call to `k_poll` will wait for to be
fulfilled.

Poll events can be initialized using either the runtime initializers
`K_POLL_EVENT_INITIALIZER()` or `k_poll_event_init`, or
the static initializer `K_POLL_EVENT_STATIC_INITIALIZER()`. An object
that matches the **type** specified must be passed to the initializers. The
**mode** *must* be set to `K_POLL_MODE_NOTIFY_ONLY`. The state
*must* be set to `K_POLL_STATE_NOT_READY` (the initializers take care
of this). The user **tag** is optional and completely opaque to the API: it is
there to help a user to group similar events together. Being optional, it is
passed to the static initializer, but not the runtime ones for performance
reasons. If using runtime initializers, the user must set it separately in the
`k_poll_event` data structure. If an event in the array is to be
ignored, most likely temporarily, its type can be set to
`K_POLL_TYPE_IGNORE`.

```c

struct k_poll_event events[4] = {
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_SEM_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_sem, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_FIFO_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_fifo, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_MSGQ_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_msgq, 0),
    K_POLL_EVENT_STATIC_INITIALIZER(K_POLL_TYPE_PIPE_DATA_AVAILABLE,
                                    K_POLL_MODE_NOTIFY_ONLY,
                                    &my_pipe, 0),
};
```
or at runtime

```c

struct k_poll_event events[4];
void some_init(void)
{
    k_poll_event_init(&events[0],
                      K_POLL_TYPE_SEM_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_sem);

    k_poll_event_init(&events[1],
                      K_POLL_TYPE_FIFO_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_fifo);

    k_poll_event_init(&events[2],
                      K_POLL_TYPE_MSGQ_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_msgq);

    k_poll_event_init(&events[3],
                      K_POLL_TYPE_PIPE_DATA_AVAILABLE,
                      K_POLL_MODE_NOTIFY_ONLY,
                      &my_pipe);

    // tags are left uninitialized if unused
}
```
After the events are initialized, the array can be passed to
`k_poll`. A timeout can be specified to wait only for a specified
amount of time, or the special values `K_NO_WAIT` and
`K_FOREVER` to either not wait or wait until an event condition is
satisfied and not sooner.

A list of pollers is offered on each semaphore or FIFO and as many events
can wait in it as the app wants.
Notice that the waiters will be served in first-come-first-serve order,
not in priority order.

In case of success, `k_poll` returns 0. If it times out, it returns
-`EAGAIN`.

```c

// assume there is no contention on this semaphore and FIFO
// -EADDRINUSE will not occur; the semaphore and/or data will be available

void do_stuff(void)
{
    rc = k_poll(events, ARRAY_SIZE(events), K_MSEC(1000));
    if (rc == 0) {
        if (events[0].state == K_POLL_STATE_SEM_AVAILABLE) {
            k_sem_take(events[0].sem, 0);
        } else if (events[1].state == K_POLL_STATE_FIFO_DATA_AVAILABLE) {
            data = k_fifo_get(events[1].fifo, 0);
            // handle data
        } else if (events[2].state == K_POLL_STATE_MSGQ_DATA_AVAILABLE) {
            ret = k_msgq_get(events[2].msgq, buf, K_NO_WAIT);
            // handle data
        } else if (events[3].state == K_POLL_STATE_PIPE_DATA_AVAILABLE) {
            bytes_read = k_pipe_read(events[3].pipe, buf, bytes_to_read, K_NO_WAIT);
            // handle data
        }
    } else {
        // handle timeout
    }
}
```
When `k_poll` is called in a loop, the events state must be reset
to `K_POLL_STATE_NOT_READY` by the user.

```c

void do_stuff(void)
{
    for(;;) {
        rc = k_poll(events, ARRAY_SIZE(events), K_FOREVER);
        if (events[0].state == K_POLL_STATE_SEM_AVAILABLE) {
            k_sem_take(events[0].sem, 0);
        }
        if (events[1].state == K_POLL_STATE_FIFO_DATA_AVAILABLE) {
            data = k_fifo_get(events[1].fifo, 0);
            // handle data
        }
        if (events[2].state == K_POLL_STATE_MSGQ_DATA_AVAILABLE) {
            ret = k_msgq_get(events[2].msgq, buf, K_NO_WAIT);
            // handle data
        }
        if (events[3].state == K_POLL_STATE_PIPE_DATA_AVAILABLE) {
            bytes_read = k_pipe_read(events[3].pipe, buf, bytes_to_read, K_NO_WAIT);
            // handle data
        }
        events[0].state = K_POLL_STATE_NOT_READY;
        events[1].state = K_POLL_STATE_NOT_READY;
        events[2].state = K_POLL_STATE_NOT_READY;
        events[3].state = K_POLL_STATE_NOT_READY;
    }
}
```

### Using k_poll_signal_raise()


One of the types of events is `K_POLL_TYPE_SIGNAL`: this is a "direct"
signal to a poll event. This can be seen as a lightweight binary semaphore only
one thread can wait for.

A poll signal is a separate object of type `k_poll_signal` that
must be attached to a k_poll_event, similar to a semaphore or FIFO. It must
first be initialized either via `K_POLL_SIGNAL_INITIALIZER()` or
`k_poll_signal_init`.

```c

struct k_poll_signal signal;
void do_stuff(void)
{
    k_poll_signal_init(&signal);
}
```
It is signaled via the `k_poll_signal_raise` function. This function
takes a user **result** parameter that is opaque to the API and can be used to
pass extra information to the thread waiting on the event.

```c

struct k_poll_signal signal;

// thread A
void do_stuff(void)
{
    k_poll_signal_init(&signal);

    struct k_poll_event events[1] = {
        K_POLL_EVENT_INITIALIZER(K_POLL_TYPE_SIGNAL,
                                 K_POLL_MODE_NOTIFY_ONLY,
                                 &signal),
    };

    k_poll(events, 1, K_FOREVER);

    int signaled, result;

    k_poll_signal_check(&signal, &signaled, &result);

    if (signaled && (result == 0x1337)) {
        // A-OK!
    } else {
        // weird error
    }
}

// thread B
void signal_do_stuff(void)
{
    k_poll_signal_raise(&signal, 0x1337);
}
```
If the signal is to be polled in a loop, *both* its event state must be
reset to `K_POLL_STATE_NOT_READY` *and* its `result` must be
reset using `k_poll_signal_reset()` on each iteration if it has
been signaled.

```c

struct k_poll_signal signal;
void do_stuff(void)
{
    k_poll_signal_init(&signal);

    struct k_poll_event events[1] = {
        K_POLL_EVENT_INITIALIZER(K_POLL_TYPE_SIGNAL,
                                 K_POLL_MODE_NOTIFY_ONLY,
                                 &signal),
    };

    for (;;) {
        k_poll(events, 1, K_FOREVER);

        int signaled, result;

        k_poll_signal_check(&signal, &signaled, &result);

        if (signaled && (result == 0x1337)) {
            // A-OK!
        } else {
            // weird error
        }

        k_poll_signal_reset(&signal);
        events[0].state = K_POLL_STATE_NOT_READY;
    }
}
```
Note that poll signals are not internally synchronized. A `k_poll` call
that is passed a signal will return after any code in the system calls
`k_poll_signal_raise()`.  But if the signal is being
externally managed and reset via `k_poll_signal_init()`, it is
possible that by the time the application checks, the event state may
no longer be equal to `K_POLL_STATE_SIGNALED`, and a (naive)
application will miss events.  Best practice is always to reset the
signal only from within the thread invoking the `k_poll` loop, or else
to use some other event type which tracks event counts: semaphores and
FIFOs are more error-proof in this sense because they can't "miss"
events, architecturally.
