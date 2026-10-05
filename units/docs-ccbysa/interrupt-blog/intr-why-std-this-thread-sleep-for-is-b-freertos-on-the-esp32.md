---
id: "intr-why-std-this-thread-sleep-for-is-b-freertos-on-the-esp32"
type: "concept"
domain: "debug"
title: "Why std::this_thread::sleep_for() is broken on ESP32: FreeRTOS on the ESP32"
summary: "Let's go into some background first. Experienced embedded engineers will likely find parts of this section as a review, but we need to be solid in our understanding of the fundamentals before moving on."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-20-why-sleep-for-is-broken-on-esp32.md"
doc_source: "https://interrupt.memfault.com/blog/why-sleep-for-is-broken-on-esp32#freertos-on-the-esp32"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's go into some background first. Experienced embedded engineers will likely
find parts of this section as a review, but we need to be solid in our
understanding of the fundamentals before moving on.

### System Tick Period

My project is set to the default ESP32 FreeRTOS tick period of 10 milliseconds,
represented by the `portTICK_PERIOD_MS` macro:

```c
#define CONFIG_FREERTOS_HZ 100 /* sdkconfig.h */
#define configTICK_RATE_HZ CONFIG_FREERTOS_HZ /* FreeRTOSConfig.h */
#define portTICK_PERIOD_MS ((uint32_t)1000 / configTICK_RATE_HZ) /* portmacro.h */
```

This is used by ESP32 to setup the system tick (systick) interrupt, done by
`vSystimerSetup()` in `components\freertos\port_systick.c`. Notably, there are
two system ticks because there are two cores. Here is the interesting part done
for each core:

```c
/* configure the timer */
uint32_t alarm_id = SYSTIMER_ALARM_OS_TICK_CORE0 + cpuid;
systimer_hal_connect_alarm_counter(&systimer_hal, alarm_id, SYSTIMER_COUNTER_OS_TICK);
systimer_hal_set_alarm_period(&systimer_hal, alarm_id, 1000000UL / CONFIG_FREERTOS_HZ);
systimer_hal_select_alarm_mode(&systimer_hal, alarm_id, SYSTIMER_ALARM_MODE_PERIOD);
```

Obviously, by "sleeping" a thread for a period of time, we want to _yield_
execution to other threads. This is accomplished by the
[FreeRTOS scheduler](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#smp-scheduler).
The basic unit of the scheduler is the system tick period. Other things can
occur based on interrupts as well, but terms of sleeping threads, the system
tick period is what really matters.

ESP32's FreeRTOS scheduler is running a
[Best Effort Round Robin time slicing](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#time-slicing)
algorithm. This is slightly different than the standard FreeRTOS algorithm
("best effort" instead of perfect) due to
[symmetric-multiprocessing](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/freertos_idf.html#symmetric-multiprocessing).
The important bit to note here is even when a thread does _not_ explicitly
yield, the scheduler will
[time slice](https://interrupt.memfault.com/blog/<https://en.wikipedia.org/wiki/Preemption_(computing)#Time_slice>)
amongst the highest priority ready-state threads on the system tick period
intervals.

### Small Sleeps and Delays

The following code yields the minimal amount of time:

```c
vTaskDelay(1);
```

This will guarantee the thread will sleep _at least_ until the next system tick
interrupt.

But when is the next system tick interrupt in relation to the execution of
`vTaskDelay(1)`? It could be in 1 nanosecond, all the way up to our system tick
period of 10 milliseconds. Exactly how much time the thread will be sleep is
unknown to this code.

So to be clear: sleeping _"1 tick"_ does not mean it will sleep for one tick
_period of time_. In fact, it will always sleep some amount less than one tick
period, and sometimes it will not sleep at all.

So then, is calling `vTaskDelay(1)` in a small loop a problem? Not
intrinsically. Like most things, it's fine if you know what you are doing. If
you want to ensure a thread (technically called a
[Task](https://www.freertos.org/Documentation/02-Kernel/02-Kernel-features/01-Tasks-and-co-routines/00-Tasks-and-co-routines)
in FreeRTOS) executes its logic is performed on every tick, this a way to do it.
There are no problems so long as the logic is not sensitive to tick jitter and
its processing only requires a small fraction of the tick period.

We could attempt to be more idiomatic by using code like this:

```c
vTaskDelay(pdMS_TO_TICKS(10));
```

The macro `pdMS_TO_TICKS()` converts milliseconds into ticks by accounting for
the FreeRTOS configuration tick period. If the period changes or, god forbid,
the code is copied and pasted into a different project, the proper tick count
would be calculated. If our tick period is 10 milliseconds it will call
`vTaskDelay(1)`. All is great.

Except not always. Say we want to sleep 9 milliseconds. If we write
`vTaskDelay(pdMS_TO_TICKS(9))` the macro will actually call `vTaskDelay(0)`.
This is because it does integer math:

```c
typedef uint32_t TickType_t;
#define pdMS_TO_TICKS( xTimeInMs )    ( ( TickType_t ) ( ( ( TickType_t ) ( xTimeInMs ) * ( TickType_t ) configTICK_RATE_HZ ) / ( TickType_t ) 1000U ) )
```

So `(9*100)/1000 = 0.9`, but as a `uint32_t`, just `0`. This is certainly not
what we want, because passing `0` to `vTaskDelay()` does nothing at all.

Okay, but what if we _really_ need to wait for less than a tick period? We can
[busy wait](https://en.wikipedia.org/wiki/Busy_waiting). The IDF has
`esp_rom_delay_us()`, which does just that. But this is an
[Internal API](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/internal-unstable.html)
which we don't have source code for, and its functionality may change or be
removed in the future. ESP does give us `usleep()` though, and that allows
precise delays. The caveat here is that the FreeRTOS scheduler is still free to
context switch out of the busy loop due to the important bit I said above about
time slicing. If you must _absolutely_ guarantee timing, then you must disable
the FreeRTOS scheduler (and perhaps all interrupts) for that period.

The other option is to use a free running timer and trigger an interrupt when it
expires. The interrupt can signal FreeRTOS to wake the waiting task. This is
great as long as your context switch overheads allow it and you have a free
hardware timer to do it.

All of this is to say the following:

1. If you care about precision timing, details matter.
2. If you _don't care_ about precision timing but are using it, you are probably
   wasting resources.
