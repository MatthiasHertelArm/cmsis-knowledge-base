---
id: "intr-why-std-this-thread-sleep-for-is-b-idf-newlib"
type: "concept"
domain: "debug"
title: "Why std::this_thread::sleep_for() is broken on ESP32: IDF Newlib"
summary: "A few things to unpack here which lead us into Newlib. Let's start with how chrono::steady_clock::now() works."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-20-why-sleep-for-is-broken-on-esp32.md"
doc_source: "https://interrupt.memfault.com/blog/why-sleep-for-is-broken-on-esp32#idf-newlib"
license: "CC-BY-SA-4.0"
mode: "V"
---

A few things to unpack here which lead us into Newlib. Let's start with how
`chrono::steady_clock::now()` works.

### `clock_gettime()`

Calling `chrono::steady_clock::now()` on the ESP32 is just a wrapper for
`clock_gettime()` located in `newlib` (`idf/components/newlib/time.c`), where
`clock_id` is `CLOCK_MONOTONIC`.

```c
int clock_gettime(clockid_t clock_id, struct timespec *tp)
{
#if IMPL_NEWLIB_TIME_FUNCS
    if (tp == NULL) {
        errno = EINVAL;
        return -1;
    }
    struct timeval tv;
    uint64_t monotonic_time_us = 0;
    switch (clock_id) {
    case CLOCK_REALTIME:
        _gettimeofday_r(NULL, &tv, NULL);
        tp->tv_sec = tv.tv_sec;
        tp->tv_nsec = tv.tv_usec * 1000L;
        break;
    case CLOCK_MONOTONIC:
        monotonic_time_us = esp_time_impl_get_time();
        tp->tv_sec = monotonic_time_us / 1000000LL;
        tp->tv_nsec = (monotonic_time_us % 1000000LL) * 1000L;
        break;
    default:
        errno = EINVAL;
        return -1;
    }
    return 0;
#else
    errno = ENOSYS;
    return -1;
#endif
}
```

Calling `esp_time_impl_get_time()` gets a value based on a free-running hardware
timer with at least 1 us accuracy. So that is how the monotonic clock is
implemented on the ESP32. Note that this clock is completely independent of the
timer that is controlling the FreeRTOS system tick interrupt. No problems there.

### `sleep()`

ESP32 implements `sleep()` as a simple wrapper of `usleep()`:

```c
unsigned int sleep(unsigned int seconds)
{
    usleep(seconds * 1000000UL);
    return 0;
}
```

### `usleep()`

Okay, so in both versions of IDF, `usleep()` is at the bottom of all sleeping
calls. Here it is:

```c
int usleep(useconds_t us)
{
    const int64_t us_per_tick = portTICK_PERIOD_MS * 1000;
    if (us < us_per_tick) {
        esp_rom_delay_us((uint32_t) us);
    } else {
        /* since vTaskDelay(1) blocks for anywhere between 0 and portTICK_PERIOD_MS,
         * round up to compensate.
         */
        vTaskDelay((us + us_per_tick - 1) / us_per_tick);
    }
    return 0;
}
```

Remember when I said that `esp_rom_delay_us()` is an internal API and we should
use `usleep()` instead? Well, `usleep()` is just a wrapper to
`esp_rom_delay_us()` for short periods (e.g. less than one tick period). We can
consider `usleep()` the "public" exposure of `esp_rom_delay_us()`, but only when
the specified time is less than a system tick period. As mentioned above, this
is a busy wait, and since it does not disable the scheduler, it still allows
other threads _of equal or higher priority_ to run. So, the timing represents a
guaranteed _minimum_ only. More importantly, if there are other threads of lower
priority, it will _not_ context switch during this busy time. It will just sit
in the thread until the wait is over.

This is all good. A guaranteed minimum is how I expect `usleep()` to work.

In terms of blocking vs yielding, IDF
[docs](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/pthread.html?#rtos-integration)
say:

> When calling a standard libc or C++ sleep function, such as usleep defined in
> unistd.h, the task will only block and yield the core if the sleep time is
> longer than one FreeRTOS tick period. If the time is shorter, the thread will
> busy-wait instead of yielding to another RTOS task.

It should say for sleeping _equal to_ or longer than one tick period cause
yielding vs. busy waiting. In any case, the yielding is done via `vTaskDelay()`.

There is a problem here though. The ticks to yield calculations often produce
times yielded _less than_ the specified amount.

Let's play out an example. If we wanted to sleep for 15 milliseconds, the
calculations would give us `vTaskDelay(2)`:

1. `portTICK_PERIOD_MS` is defined as `10`. So `us_per_tick` is `10,000`.
2. `us` is `15000`
3. `(15000 + 10000 - 1) / 10000)` is `(24999) / 10000` which gives `2.4999`
4. But since we are using integers, it is just `2`

But what does `2` mean? It means two occurrences of the tick interrupt. Once
again, we can ask: when is the next tick interrupt from the moment that
`vTaskDelay(2)` is called? The tick interrupt could be in 1 nanosecond all the
way up to 10 milliseconds from now. After that, the second tick will be the
system tick period of 10 milliseconds. So for a tick count of `2`, we will
actually sleep between between 10 and 20 milliseconds.

Even though the comment says it is rounding up to compensate for the first tick
potentially not blocking at all, the compensation does not account for the
worse-case minimal timing. In the example I gave, a 15-millisecond request will
sometimes only sleep for 10 milliseconds. Likewise, a 10 millisecond `usleep()`
will sometimes sleep about 0 milliseconds. The greatest _potential_ differential
comes with calling `usleep()` with a multiple of the tick period. In that case,
the time spent may be short by an entire tick period.

Whether this "shorter than specified" time matters depends on requirements. In
my experience, a lot of application-level logic would probably be fine with a
"10 to 20" millisecond wait. On the other hand, hardware driver logic and audio
pipelines have specific realtime characteristics where this would absolutely be
a problem.

According to `man 3 sleep` and
[POSIX](https://pubs.opengroup.org/onlinepubs/009695399/functions/usleep.html),
`usleep()` should always sleep _at least_ the time specified. It is allowed to
sleep more if needed.

> The usleep() function shall cause the calling thread to be suspended from
> execution until either the number of realtime microseconds specified by the
> argument useconds has elapsed or a signal is delivered to the calling thread
> and its action is to invoke a signal-catching function or to terminate the
> process. The suspension time may be longer than requested due to the
> scheduling of other activity by the system.

The fact that ESP32's IDF `usleep()` can be short by up to one system tick
period means it doesn't follow the specifications.
