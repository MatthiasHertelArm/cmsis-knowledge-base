---
id: "intr-why-std-this-thread-sleep-for-is-b-would-you-like-precision-or-efficiency"
type: "concept"
domain: "debug"
title: "Why std::this_thread::sleep_for() is broken on ESP32: Would You Like Precision or Efficiency?"
summary: "In IDF v4, calling std::this_thread::sleep_for() calls usleep() once. When std::this_thread::sleep_for(10ms) is executed, it calls vTaskDelay(1), and the thread will sleep between 0 and 10 milliseconds. It will usually sleep for less than the time specified."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-20-why-sleep-for-is-broken-on-esp32.md"
doc_source: "https://interrupt.memfault.com/blog/why-sleep-for-is-broken-on-esp32#would-you-like-precision-or-efficiency"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's recap.

In IDF v4, calling `std::this_thread::sleep_for()` calls `usleep()` once. When
`std::this_thread::sleep_for(10ms)` is executed, it calls `vTaskDelay(1),` and
the thread will sleep between 0 and 10 milliseconds. It will usually sleep for
less than the time specified.

In IDF v5, calling `std::this_thread::sleep_for(10ms)` almost always calls
`usleep()` _twice_. The first time will use `vTaskDelay(1)`, and it will usually
sleep for less than the time specified. Then, back in `libstdc++`
`__sleep_for()`, the monotonic clock will be checked and it will be seen that
some fractional component of 10 milliseconds remains, causing a second call to
`usleep()`. The second call will always be with a time less than the system tick
period. This will cause a blocking call to `esp_rom_delay_us()`. That blocking
call is the problem.

Let's break it down further. For a 10 millisecond delay:

1. `(10000 + 10000 - 1) / 10000)` is `(19999) / 10000` which gives `1.9999`
2. But since we are using integers, it is just `1`

But once again, saying `vTaskDelay(1)` means "wait for 1 tick interrupt." That
will almost always be less than 10 milliseconds from now. When `vTaskDelay(1)`
returns, somewhere between 0.000001 and 10.000000 milliseconds will have
actually transpired. The newer version of `__sleep_for()` in IDF v5 / GCC 13
will double-check that the correct time has actually elapsed according to the
monotonic clock. That check will fail, so it calls `usleep()` again, this time
with the remainder of the 10 milliseconds. The specified time is less than a
system tick period, so the blocking `esp_rom_delay_us()` is now called.

So what about time slicing? Even if `esp_rom_delay_us()` blocks, the FreeRTOS
scheduler can switch to another task. Firstly, if this thread is of a higher
priority, _no lower priorities will ever run_. But even if everything is of the
same priority, the CPU will just switch back to the blocking call on the next
round robin, continuing the blocking wait. In our current scenario, this is
horribly inefficient, unnecessary, and unexpected.

Any call to `sleep_for()` greater than the tick period has this problem because
the tick interrupt is asynchronous to the `sleep_for()` call. This means when
the scheduler returns from `vTaskDelay()` some random remainder of time will be
done with `esp_rom_delay_us()` in order to sleep for the _precise_ amount of
time requested.

The new version of `sleep_for()` is much more precise, but it is at the cost of
computing efficiency on the ESP32 because some fraction of the tick period will
be _busy waited_ instead of yielded. That is very bad to do on an MCU.

Of course, none of this is transparent to the application code, and I doubt it
was something intentional from Espressif. It is just a consequence of upgrading
to a new version of GCC combined with how IDF implements `usleep()`.
